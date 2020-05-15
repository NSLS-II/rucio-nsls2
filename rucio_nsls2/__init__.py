import event_model
import databroker.core

from rucio.client.didclient import DIDClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.utils import adler32
from ._version import get_versions
from area_detector_handlers import HDF5DatasetSliceHandlerPureNumpy

__version__ = get_versions()['version']
del get_versions

rse='BLUESKY'
scope='bluesky-nsls2'
dataset='bluesky-sdcc',
pfn='globus:///~/globus/'


class HDF5DatasetSliceHandlerPureNumpyLazy(HDF5DatasetSliceHandlerPureNumpy):
    def __init__(self, filename, frame_per_point=1):
        self._fpp = frame_per_point
        self._filename = filename
        self._file = None
        self._dataset = None
        self._data_objects = {}


def _get_filenames(run):
    files = []
    run.fillers['yes'].register_handler('AD_HDF5', HDF5DatasetSliceHandlerPureNumpyLazy, overwrite=True)
    for name, doc in run.canonical(fill='no'):
        if name == 'resource':
            files.extend(run.get_file_list(doc))
    return files


def _rucio_register(self, filenames):
    files = []
    dids = []

    for filename in filenames:
        size = os.stat(str(filename)).st_size
        adler = adler32(str(filename))
        files.append({'scope': self.scope, 'name': str(filename.parts[-1]),
                      'bytes': size, 'adler32': adler,
                      'pfn': self.pfn + str(filename.parts[-1])})

    replica_client = ReplicaClient()
    replica_client.add_replicas(rse=self.rse, files=files)
    didclient = DIDClient()
    didclient.add_files_to_dataset(self.scope, self.dataset, files)


def cache_runs(catalog, run_uids, lifetime):
    files = []
    for run_uid in run_uids:
        run = catalog[run_uid]
        files.extend(_get_filenames(run))
    _rucio_register(files)


def cache_catalog(catalog, lifetime):
    files = []
    for run_uid in list(catalog):
        run = catalog[run_uid]
        files.extend(_get_filenames(run))
    _rucio_register(files)


