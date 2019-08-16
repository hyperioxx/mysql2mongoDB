from mysql2mongodb.databases.mysql import Database



db = Database(address="", user="", password="", database_name="")

print(db.tables()[26].export())