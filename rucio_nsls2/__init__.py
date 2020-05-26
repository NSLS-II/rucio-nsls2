import event_model
import databroker.core
import os

from rucio.client.didclient import DIDClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.utils import adler32
from ._version import get_versions
from .roots import dtn_map
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
    resource_path = os.path.join(root, resource_path)
    for old_root in sorted(dtn_map[beamline].keys(), key=len, reverse=True):
        temp_root = os.path.join(old_root, '')
        if temp_root == resource_path[:len(temp_key)]
            if dtn_map[old_root] is None:
                raise ValueError(f"Files not available for beamline {beamline} with root {key}")
            resource_path.replace(temp_root, os.path.join(dtn_map[old_root], '')

    handler = handler_class(resource_path,
                            **resource['resource_kwargs'])

    def datum_kwarg_gen():
        for page in run._get_datum_pages(resource['uid']):
            for datum in event_model.unpack_datum_page(page):
                yield datum['datum_kwargs']

    files.extend(handler.get_file_list(datum_kwarg_gen()))
    return files


def _get_filenames(beamline_name, run):
    """
    Get the list of filenames for a run.
    """
    files = []
    run.fillers['yes'].register_handler('AD_HDF5', HDF5DatasetSliceHandlerPureNumpyLazy, overwrite=True)
    for name, doc in run.canonical(fill='no'):
        if name == 'resource':
            files.extend(_get_file_list(beamline_name, run, doc))
    return files


def _rucio_register(filenames):
    """
    Register the file in rucio for replication to SDCC.
    """
    files = []
    dids = []

    for filename in filenames:
        #size = os.stat(str(filename)).st_size
        #adler = adler32(str(filename))
        files.append({'scope': scope, 'name': str(filename.parts[-1]),
                      'bytes': 1000, 'adler32': "unknown",
                      'pfn': pfn + filename})

    replica_client = ReplicaClient()
    replica_client.add_replicas(rse=rse, files=files)
    didclient = DIDClient()
    didclient.add_files_to_dataset(scope, dataset, files)


def cache_runs(catalog, run_uids, lifetime):
    """
    Replicate the files for the list of runs given at SDCC.
    """
    files = []
    for run_uid in run_uids:
        run = catalog[run_uid]
        files.extend(_get_filenames(run))
    _rucio_register(files)


def cache_catalog(catalog, lifetime):
    """
    Replicate all of the catalog's files at SDCC.
    """
    files = []
    for run_uid in list(catalog):
        run = catalog[run_uid]
        files.extend(_get_filenames(run))
    _rucio_register(files)


