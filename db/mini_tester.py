import mysql.connector
from Connection import Connection

test = Connection()

try:
    all_films = "SELECT * FROM Film"
    penelope_films = "SELECT first_name as nome, last_name as cognome, title as film FROM actor a INNER JOIN film_actor fa ON a.actor_id = fa.actor_id INNER JOIN film f ON f.film_id = fa.film_id WHERE first_name = 'PENELOPE' and last_name = 'GUINESS'"

    # mia_connessione = Connection(
    #     host='localhost', user='root', password='Leagueofdraven19', port='3306', database='sakila')
    test.executeQuery(penelope_films)
    results = test.executeQuery(penelope_films)

    for result in results:
        print(result)

except mysql.connector.Error as errore:
    print("Si è verificato un errore")
    print(errore)
finally:
    test.close()
    print("connessione chiusa")
