import MySQLdb
from ..base import Database

class MysqlDatabase:

    def __init__(self, address="localhost", port=3306, user=None, password=None, database_name=None):
        self._cursor = None
        self._connect(address=address, port=port, user=user, password=password, database_name=database_name)
        self._tables = self._get_tables()


    def __getitem__(self, key):
        return self._tables[key]

    def __setitem__(self, key, value):
        raise Exception("MysqlDatabase instance cannot be added too!")

    def _connect(self, address="localhost", port=3306, user=None, password=None, database_name=None):
        try:
            self._db = MySQLdb.connect(host=address, user=user, passwd=password, port=port, db=database_name)
            self._cursor = self._db.cursor()
        except Exception as err:
            print(err)

    def _get_tables(self):
        temp_dict = {}
        query = "SHOW TABLES;"
        for table in self.send_query(query):
            temp_dict[table[0]] = Table(cursor=self._cursor, table_name=table[0])
        return temp_dict

    def tables(self):
        return self._tables

    def send_query(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchall()

        
class Table:
    
    def __init__(self, cursor=None, table_name=None):
        self._table_name = table_name
        self._cursor = cursor
        self._columns = []
        self._get_columns()
        self._data = []

    def _get_columns(self):
        query = "SHOW columns FROM {}".format(self._table_name)
        for column in self.send_query(query):
            self._columns.append(column[0])

    def columns(self):
        return self._columns

    def name(self):
        return self._table_name

    def send_query(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchall()


    def export(self):
        query = "SELECT * FROM {};".format(self._table_name)
        for row in self.send_query(query):
            self._data.append(dict(zip(self._columns, row)))
        return self._data





    
        



