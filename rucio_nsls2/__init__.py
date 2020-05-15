import event_model
import databroker.core

from rucio.client.didclient import DIDClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.utils import adler32
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions


def nsls2_to_sdcc(catalog, lifetime, handler_registry=None):
    for run in catalog:
        files = get_file_names(run, handler_registry)
        rucio_replication(files)


def _get_file_names(run, handler_registry):



def _rucio_replication(files):
a


def rucio_register(self, filenames):
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
