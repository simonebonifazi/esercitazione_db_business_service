import mysql.connector
from connection import Connection


class Query(Connection):
    def get_all_actors(self):
        query_actors = "select * from Actor"
        Connection().execute_query(self, query_actors)

    def get_all_film(self):
        query_films = "select * from Film"
        Connection().execute_query(self, query_films)


test = Query()

try:
    all_films = "SELECT * FROM Film"
    penelope_films = "SELECT first_name as nome, last_name as cognome, title as film FROM actor a INNER JOIN film_actor fa ON a.actor_id = fa.actor_id INNER JOIN film f ON f.film_id = fa.film_id WHERE first_name = 'PENELOPE' and last_name = 'GUINESS'"

    test.execute_query(penelope_films)
    results = test.execute_query(penelope_films)

    for result in results:
        print(result)

except mysql.connector.Error as errore:
    print("Si è verificato un errore")
    print(errore)
finally:
    test.close()
    print("connessione chiusa")
