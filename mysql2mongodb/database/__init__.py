from .mysql import MysqlDatabase
from .mongodb import MongoDatabase

class DatabaseFactory:
    """
    Database Factory returns requested database instance 

    """

    @staticmethod
    def build(build, address="localhost", user="foo", password="bar", database_name=None):
        if build == "mysql":
            return MysqlDatabase(address=address, user=user, password=password, database_name=database_name)
        elif build == "mongodb":
            return MongoDatabase(address=address, user=user, password=password, database_name=database_name)
        else:
            return NullDatabase(address=address, port=port, user=user, password=password, database_name=database_name)



class NullDatabase:

    def __init__(self, address="localhost", port=27017, user="foo", password="bar", database_name=None):
        pass

