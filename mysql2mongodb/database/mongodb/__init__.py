import pymongo
import logging


class MongoDatabase:

    def __init__(self, address="localhost", port=27017, user=None, password=None, database_name=None):
        self._log = logging.getLogger(__name__)
        self._client = None
        self._connect(address=address, port=port, user=user, password=password, database_name=database_name)
        pass

    def _connect(self, address, port, user, password, database_name):
        self._client = pymongo.MongoClient(address, port)
        self._database = self._client[database_name]



class Collection:
    pass