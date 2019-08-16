import MySQLdb

class Database:

    def __init__(self, address="localhost", port=3306, user=None, password=None, database_name=None):
        self._cursor = None
        self._connect(address=address, port=port, user=user, password=password, database_name=database_name)
        self._tables = self._get_tables()

    def _connect(self, address="localhost", port=3306, user=None, password=None, database_name=None):
        try:
            self._db = MySQLdb.connect(host=address, user=user, passwd=password, port=port, db=database_name)
            self._cursor = self._db.cursor()
        except Exception as err:
            print(err)

    def _get_tables(self):
        temp_list = []
        query = "SHOW TABLES;"
        self._cursor.execute(query)
        for table in self._cursor.fetchall():
            temp_list.append(Table(cursor=self._cursor, table_name=table[0]))
        return temp_list

    def tables(self):
        return self._tables

        
class Table:
    
    def __init__(self, cursor=None, table_name=None):
        self._table_name = table_name
        self._cursor = cursor
        self._columns = []
        self._get_columns()
        self._data = []

    def _get_columns(self):
        query = "SHOW columns FROM {}".format(self._table_name)
        self._cursor.execute(query)
        for column in self._cursor.fetchall():
            self._columns.append(column[0])

    def columns(self):
        return self._columns


    def export(self):
        query = "SELECT * FROM {};".format(self._table_name)
        self._cursor.execute(query)
        for row in self._cursor.fetchall():
            self._data.append(dict(zip(self._columns, row)))
        return self._data



    
        



