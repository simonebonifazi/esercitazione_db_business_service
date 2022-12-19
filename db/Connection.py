import mysql.connector
import json


class Connection:

    def __init__(self, **config):
        self.connection = None
        with open('db/config.json', 'r') as k:
            config = json.load(k)
        self.connection = mysql.connector.connect(**config)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        if self.connection != None:
            self.connection.close()
