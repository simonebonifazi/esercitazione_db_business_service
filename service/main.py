import mysql.connector
import json


class Connection:

    def __init__(self, ):
        self.connection = None
        with open('db/config.json', 'r') as k:
            config = json.load(k)
        self.connection = mysql.connector.connect()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        if self.connection != None:
            self.connection.close()


class Query(Connection):
    def get_all_actors(self):
        query_actors = "select * from Actor"
        Connection().execute_query(self, query_actors)

    def get_all_film(self):
        query_films = "select * from Film"
        Connection().execute_query(self, query_films)


class Printer(Query):
    def print_all_actors(self):
        result = Query().get_all_actors(self)
        for i in result:
            print(i)

    def print_all_film(self):
        result = Query().get_all_film(self)
        for i in result:
            print(i)


printer = Printer()

try:
    test = printer.print_all_actors()
    printer.execute_query(test)
    results = printer.execute_query(test)

    for result in results:
        print(result)

except mysql.connector.Error as errore:
    print("Si è verificato un errore")
    print(errore)
finally:
    printer.close()
    print("connessione chiusa")
