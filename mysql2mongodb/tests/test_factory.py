from mysql2mongodb.database import DatabaseFactory
import mysql2mongodb


def mysql_init(self, address="localhost", port=3306, user=None, password=None, database_name=None):
    """
    Used to monkey patch new constructor for MysqlDatabase class
        :param self: 
        :param address="localhost": 
        :param port=3306: 
        :param user=None: 
        :param password=None:
        :param database_name=None: 
    """
    self._log = None
    self._cursor = None
    self._tables = None



def test_database_factory_mysql():
    mysql2mongodb.database.mysql.MysqlDatabase.__init__ = mysql_init
    if type(DatabaseFactory.build('mysql')) == type(mysql2mongodb.database.mysql.MysqlDatabase()):
        assert True
    else:
        assert False