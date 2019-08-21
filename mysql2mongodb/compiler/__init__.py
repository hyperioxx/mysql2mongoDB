import sqlparse 

class Mysql2MongoDBCompiler:

    def __init__(self, sql=None):
        self._sql = sql
        self.tokenize(sql)

    def tokenize(self, raw):
        self.tokens = sqlparse.parse(sqlparse.format(raw, keyword_case='upper'))[0]

    def compile(self):
        if str(self.tokens[0].ttype) not in ("Token.Keyword.DML" ,"Token.Keyword"):
            print("Invalid SQL syntax!!")
            print()
            return
        for token in self.tokens:
            print(token.ttype)

    