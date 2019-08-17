#!/usr/bin/python3
import getpass
import os
from cmd2 import Cmd
from mysql2mongodb.database import DatabaseFactory
from mysql2mongodb.logging import Mysql2MongoLogging


class MySql2MongoDBApp(Cmd):
    prompt = "mysql2mongoDB> "
    mysql = None
    mongo = None
    
    logger = Mysql2MongoLogging(filename = "mysql2mongoDB.log")
    

    def do_mysql(self, args):
        """ 
        Test Command
        """
        if args == "connect":
            self._create_mysql_instance()
        else:
            print("please")
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

    



