import event_model
import databroker.core
import os
import rucio.common.exception

from rucio.client.didclient import DIDClient
from rucio.client.scopeclient import ScopeClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.utils import adler32
from ._version import get_versions
from .roots import dtn_map
from .roots import root_map
from area_detector_handlers.handlers import HDF5DatasetSliceHandlerPureNumpy

__version__ = get_versions()['version']
del get_versions


rse='NSLS2'
scope='nsls2'
dataset='bluesky-sdcc',
pfn='globus://'


class HDF5DatasetSliceHandlerPureNumpyLazy(HDF5DatasetSliceHandlerPureNumpy):
    """
    Override the init so that the open method is not called.
    """
    def __init__(self, filename, frame_per_point=1):
        self._fpp = frame_per_point
        self._filename = filename
        self._file = None
        self._dataset = None
        self._data_objects = {}


def _get_file_list(beamline, run, resource):
    """
    Fetch filepaths of external files associated with this Run.
    This method is not defined on RemoteBlueskyRun because the filepaths
    may not be meaningful on a remote machine.
    This method should be considered experimental. It may be changed or
    removed in a future release.
    """
    files = []
    # TODO Once event_model.Filler has a get_handler method, use that.
    try:
        handler_class = run.fillers['yes'].handler_registry[resource['spec']]
    except KeyError as err:
        raise event_model.UndefinedAssetSpecification(
            f"Resource document with uid {resource['uid']} "
            f"refers to spec {resource['spec']!r} which is "
            f"not defined in the Filler's "
            f"handler registry.") from err

    # Apply root_map.
    resource_path = resource['resource_path']
    root = resource.get('root', '')
    root = run.fillers['yes'].root_map.get(root, root)

    # Check if beamline has files available.
    check_beamline = dtn_map.get(beamline)
    if check_beamline is None:
        raise ValueError(f"Files not available for beamline {beamline}")

    # Update the root with the dtn01 root.
    ending = ''
    resource_path = os.path.join(root, resource_path)
    for old_root in sorted(dtn_map[beamline].keys(), key=len, reverse=True):
        temp_root = os.path.join(old_root, '')
        if temp_root == resource_path[:len(temp_root)]:
            # dtn_map[old_root] is None if files are not availble on dtn01.
            if dtn_map[beamline][old_root] is None:
                raise ValueError(f"Files not available for beamline {beamline} with root {key}")
            ending = resource_path[len(temp_root):]
            resource_path = resource_path.replace(temp_root, os.path.join(dtn_map[beamline][old_root], ''))
            break

    handler = handler_class(resource_path, **resource['resource_kwargs'])

    def datum_kwarg_gen():
        for page in run._get_datum_pages(resource['uid']):
            for datum in event_model.unpack_datum_page(page):
                yield datum['datum_kwargs']

    files.extend([(root_map[beamline][root], ending, filename) 
		  for filename in handler.get_file_list(datum_kwarg_gen())])
    return files


def _get_filenames(beamline_name, run):
    """
    Get the list of filenames for a run.
    """
    files = []
    resource_count = 0
    run.fillers['yes'].register_handler('AD_HDF5', HDF5DatasetSliceHandlerPureNumpyLazy, overwrite=True)
    for name, doc in run.canonical(fill='no'):
        if name == 'resource':
            files.extend(_get_file_list(beamline_name, run, doc))
            resource_count += 1
    print(run, resource_count, files)
    return files


def _rucio_register(beamline, uid, filenames):
    """
    Register the file in rucio for replication to SDCC.
    """
    scope = beamline
    container = uid

    replica_client = ReplicaClient()
    didclient = DIDClient()
    scopeclient = ScopeClient()
    ruleclient = RuleClient()

    for root, ending, filename in filenames:
        #size = os.stat(str(filename)).st_size
        #adler = adler32(str(filename))
        files = [{'scope': scope,
                  'name': filename.split('/')[-1],
                  'bytes': 1000,
                  #'adler32': "unknown",
                  'pfn': pfn + filename}]

        dataset = os.path.join(root, ending)
        dataset = '.'.join(dataset.split('/')[1:-1])
        print("DATASET", dataset)
        breakpoint()
        try:
            scopeclient.add_scope(account='nsls2data', scope=scope)
        except rucio.common.exception.Duplicate:
            pass
       
        replica_client.add_replicas(rse=rse, files=files)

        # Create a new container if it doesn't exist.
        try:
            didclient.add_did(scope=scope, name=uid, type='container')
        except rucio.common.exception.DataIdentifierAlreadyExists:
            pass

        # Create a replication rule.
        try:
            dids = [{'scope': scope, 'name': container}]
            ruleclient.add_replication_rule(dids=dids, 
                                            copies=1, 
                                            rse_expression='SDCC', 
			                    lifetime=86400,  # Seconds
                                            account='nsls2data', 
			                    source_replica_expression='NSLS2', 
                                            purge_replicas=True, 
			                    comment='purge_replicas in 24 hours')
        except rucio.common.exception.DuplicateRule:
            pass

        # Create a new dataset if it doesn't exist.
        try:
            didclient.add_did(scope=scope, name=dataset, type='dataset')
        except rucio.common.exception.DataIdentifierAlreadyExists:
            pass

        attachment = {'scope': scope, 'name':uid,
                      'dids':[{'scope': scope, 'name': dataset}]}
        
        try:
            didclient.add_files_to_dataset(scope, dataset, files)
        except rucio.common.exception.FileAlreadyExists:
            pass

        try:
            didclient.add_datasets_to_containers([attachment])
        except rucio.common.exception.DuplicateContent:
            pass


def get_runs(catalog, beamline, run_uids):
    """
    Replicate the files for the list of runs given at SDCC.
    """
    for run_uid in run_uids:
        run = catalog[run_uid]
        files = _get_filenames(beamline, run)
        _rucio_register(beamline, run_uid, files)


def get_catalog(catalog, beamline):
    """
    Replicate all of the catalog's files at SDCC.
    """
    for run_uid in list(catalog):
        run = catalog[run_uid]
        files = _get_filenames(beamline, run)
        _rucio_register(beamline, run_uid, files)


