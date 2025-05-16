#This Python script reads user data from user_data.csv
# and inserts each user into the user_data table in your PostgreSQL database

import csv
import psycopg2
import os

DB_CONFIG = {
    "dbname": "movie_ratings_dw",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def insert_user_data(conn, user):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO user_data (
                user_id, age, gender, country, registration_date
            ) VALUES (
                %(user_id)s, %(age)s, %(gender)s, %(country)s, %(registration_date)s
            )
            ON CONFLICT (user_id) DO NOTHING;
        """, user)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "user_data.csv")

    print("Calea absolută către user_data.csv:", os.path.abspath(csv_path))
    print("Există fișierul?", os.path.exists(csv_path))

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
    except Exception as e:
        print(f"Eroare la conectare la baza de date: {e}")
        return

    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            users = [row for row in reader]
        print(f"Citite {len(users)} utilizatori din fișier.")

        for user in users:
            user['age'] = int(user['age'])
            insert_user_data(conn, user)
            print(f"Inserat utilizator: {user['user_id']}")
        conn.commit()
        print("Toți utilizatorii au fost inserați cu succes.")
    except Exception as e:
        print(f"Eroare: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()