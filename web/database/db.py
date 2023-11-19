import sqlite3 as sql

class Database:

    def __init__(self, dbname="dbase.db", conn=None, cursor=None):
        self.dbname = dbname
        self.conn = conn
        self.cursor = cursor

    def connect(self):
        self.conn = sql.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def makequery(self, query:str):
        self.cursor.executescript(query)