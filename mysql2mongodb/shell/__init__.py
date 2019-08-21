#!/usr/bin/python3
import getpass
import os
import sqlparse
from mysql2mongodb.database import DatabaseFactory
from mysql2mongodb.logging import Mysql2MongoLogging
from mysql2mongodb.compiler import Mysql2MongoDBCompiler


class MySql2MongoDBApp:
    prompt = "mysql2mongoDB> "
    
    logger = Mysql2MongoLogging(filename = "mysql2mongoDB.log")

    def pre_command(self, arg):
        pass
    
    def post_command(self, arg):
        pass
    
    def execute_command(self, arg):
        try:
            Mysql2MongoDBCompiler(sql=arg).compile()
        except IndexError:
            pass

    def cmdloop(self):
        while True:
            _input = input(self.prompt)
            self.pre_command(_input)
            self.execute_command(_input)
            self.post_command(_input)

    



