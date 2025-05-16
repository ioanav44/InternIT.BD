#This Python script connects to your PostgreSQL 
# database and runs basic data quality checks on the movie_reviews_data table.

import psycopg2

DB_CONFIG = {
    "dbname": "movie_ratings_dw",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def run_check(conn, query, description):
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchall()
        print(f"{description}: {result}")

def main():
    checks = [
        ("SELECT COUNT(*) FROM movie_reviews_data WHERE user_id IS NULL", "Null user_id"),
        ("SELECT COUNT(*) FROM movie_reviews_data WHERE movie_id IS NULL", "Null movie_id"),
        ("SELECT review_id, COUNT(*) FROM movie_reviews_data GROUP BY review_id HAVING COUNT(*) > 1", "Duplicate review_id"),
    ]
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        for query, desc in checks:
            run_check(conn, query, desc)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()