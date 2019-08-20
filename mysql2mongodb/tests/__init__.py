from mysql2mongodb.database import DatabaseFactory



def test_database_factory_mysql():
    DatabaseFactory.build('mysql')
    assert(True)