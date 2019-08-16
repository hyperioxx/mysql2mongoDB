#!/usr/bin/python3
from cmd2 import Cmd
import getpass
from mysql2mongodb.database import DatabaseFactory


class MySql2MongoDBApp(Cmd):
    prompt = "mysql2mongoDB> "
    mysql = None
    mongo = None

    def do_mysql(self, args):
        """ 
        Test Command
        """
        print(args.arg_list)
        


    def _create_mysql_instance(self):
        database_name = input("database name: ")
        address = input("address: ")
        port = input("port(default 3306):  ")
        user = input("mysql user:")
        password = getpass.getpass("Password: ")
        self.mysql = DatabaseFactory.build('mysql',address=address, user=user, password=password, database_name=database_name)
        print("success...")


    
        

    def do_connect_mongodb(self, args):
        """ 
        Test Command
        """
        database_name = input("database name: ")
        address = input("address: ")
        port = input("port(default 3306):  ")
        user = input("mysql user:")
        password = getpass.getpass("Password: ")
        self.mongo = None

    



