import mysql.connector
from business.query import Query


class Printer(Query):
    def print_all_actors(self):
        Query().get_all_actors(self)
