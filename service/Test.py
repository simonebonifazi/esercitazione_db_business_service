import mysql.connector
from business.Query import Query


class Printer(Query):
    def print_all_actors(self):
        result = Query().get_all_actors(self)
        for i in result:
            print(i[0])

    def print_all_film(self):
        result = Query().get_all_film(self)
        for i in result:
            print(i[0])


printer = Printer()

try:
    all_films = "SELECT * FROM Film"
    penelope_films = "SELECT first_name as nome, last_name as cognome, title as film FROM actor a INNER JOIN film_actor fa ON a.actor_id = fa.actor_id INNER JOIN film f ON f.film_id = fa.film_id WHERE first_name = 'PENELOPE' and last_name = 'GUINESS'"

    printer.execute_query(all_films)
    results = printer.execute_query(all_films)

    for result in results:
        print(result)

except mysql.connector.Error as errore:
    print("Si è verificato un errore")
    print(errore)
finally:
    printer.close()
    print("connessione chiusa")
