#This Python script connects to your PostgreSQL database and executes all SQL commands from the gold_layer.sql file.
#It automates the creation or update of your gold layer views, so you don’t have to run the SQL manually in pgAdmin.

import psycopg2

DB_CONFIG = {
    "dbname": "movie_ratings_dw",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def run_sql_file(conn, filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        sql = file.read()
    with conn.cursor() as cur:
        for statement in sql.split(';'):
            if statement.strip():
                cur.execute(statement)
    print(f"Rulat cu succes: {filepath}")

def main():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
    except Exception as e:
        print(f"Eroare la conectare: {e}")
        return

    try:
        # Pune aici calea către fișierul tău gold_layer.sql
        run_sql_file(conn, "ingest_bronze_silver_gold/gold_layer.sql")
    except Exception as e:
        print(f"Eroare la rulare SQL: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()