import event_model
import databroker.core

from rucio.client.didclient import DIDClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.utils import adler32
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions


rse='BLUESKY'
scope='bluesky-nsls2'
dataset='archive',
pfn='globus:///~/globus/'


def nsls2_to_sdcc(catalog, lifetime):
    for run in catalog:
        files = _get_filenames(run)
        rucio_register(files)


def _get_filenames(run):
    # The following code is from databroker-pack
    for name, doc in run.canonical(fill="no"):
        if external == "fill":
            name, doc = filler(name, doc)
            # Omit Resource and Datum[Page] because the data was
            # filled in place.
            if name in EXTERNAL_RELATED_DOCS:
                progress.update()
                continue
        elif name == "resource":
            root = root_map.get(doc["root"], doc["root"])
            unique_id = root_hash_func(doc["root"])
            if external is None:
                resource = doc.copy()
                resource["root"] = root
                files[(root, unique_id)].update(run.get_file_list(resource))
            # Replace root with a unique ID before serialization.
            # We are overriding the local variable name doc here
            # (yuck!) so that serializer(name, doc) below works on
            # all document types.
            doc = doc.copy()
            doc["root"] = unique_id                for name, doc in run.canonical(fill="no"):
        if external == "fill":
            name, doc = filler(name, doc)
            # Omit Resource and Datum[Page] because the data was
            # filled in place.
            if name in EXTERNAL_RELATED_DOCS:
                progress.update()
                continue
        elif name == "resource":
            root = root_map.get(doc["root"], doc["root"])
            unique_id = root_hash_func(doc["root"])
            if external is None:
                resource = doc.copy()
                resource["root"] = root
                files[(root, unique_id)].update(run.get_file_list(resource))
            # Replace root with a unique ID before serialization.
            # We are overriding the local variable name doc here
            # (yuck!) so that serializer(name, doc) below works on
            # all document types.
            doc = doc.copy()
                        doc["root"] = unique_id

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
