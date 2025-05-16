# This Python script reads a list of IMDb IDs from movies_list.txt, 
# fetches movie metadata from the OMDb API for each ID, and inserts
#  the results into the omdb_metadata table in your PostgreSQL database.

import requests
import time
import psycopg2
import os

API_KEY = "56254c96"
OMDB_URL = "http://www.omdbapi.com/"

# Configurare conexiune PostgreSQL - modifică cu datele tale reale!
DB_CONFIG = {
    "dbname": "movie_ratings_dw",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def get_movie_data(imdb_id):
    params = {
        "apikey": API_KEY,
        "i": imdb_id  # caută după imdbID
    }
    print(f"Trimit request pentru ID: {imdb_id}")  # DEBUG
    response = requests.get(OMDB_URL, params=params)
    print(f"Status code pentru {imdb_id}: {response.status_code}")  # DEBUG
    if response.status_code == 200:
        data = response.json()
        print(f"Răspuns OMDb pentru {imdb_id}: {data}")  # DEBUG
        if data.get("Response") == "True":
            return {
                "imdb_id": data.get("imdbID"),
                "title": data.get("Title"),
                "year": data.get("Year"),
                "rated": data.get("Rated"),
                "released": data.get("Released"),
                "runtime": data.get("Runtime"),
                "genre": data.get("Genre"),
                "director": data.get("Director"),
                "writer": data.get("Writer"),
                "actors": data.get("Actors"),
                "plot": data.get("Plot"),
                "language": data.get("Language"),
                "country": data.get("Country"),
                "awards": data.get("Awards"),
                "poster": data.get("Poster"),
                "metascore": data.get("Metascore"),
                "imdb_rating": float(data.get("imdbRating")) if data.get("imdbRating") != "N/A" else None,
                "imdb_votes": data.get("imdbVotes"),
                "type": data.get("Type"),
                "dvd": data.get("DVD"),
                "box_office": data.get("BoxOffice"),
                "production": data.get("Production"),
                "website": data.get("Website"),
            }
        else:
            print(f"Film negăsit: {imdb_id}")
            return None
    else:
        print(f"Eroare la cerere pentru {imdb_id}: {response.status_code}")
        return None

def insert_movie_data(conn, movie_data):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO omdb_metadata (
                imdb_id, title, year, rated, released, runtime, genre, director, writer,
                actors, plot, language, country, awards, poster, metascore, imdb_rating,
                imdb_votes, type, dvd, box_office, production, website
            ) VALUES (
                %(imdb_id)s, %(title)s, %(year)s, %(rated)s, %(released)s, %(runtime)s, %(genre)s, %(director)s, %(writer)s,
                %(actors)s, %(plot)s, %(language)s, %(country)s, %(awards)s, %(poster)s, %(metascore)s, %(imdb_rating)s,
                %(imdb_votes)s, %(type)s, %(dvd)s, %(box_office)s, %(production)s, %(website)s
            )
            ON CONFLICT (imdb_id) DO NOTHING;
        """, movie_data)

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    movies_path = os.path.join(current_dir, "movies_list.txt")

    print("Calea absolută către movies_list.txt:", os.path.abspath(movies_path))
    print("Există fișierul?", os.path.exists(movies_path))

    # Conectare la baza de date
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
    except Exception as e:
        print(f"Eroare la conectare la baza de date: {e}")
        return

    try:
        with open(movies_path, "r", encoding="utf-8") as file:
            imdb_ids = [line.strip() for line in file if line.strip()]

        print("ID-uri citite din fișier:", imdb_ids)
        print(f"Citite {len(imdb_ids)} filme din lista.")

        for imdb_id in imdb_ids:
            print(f"Prelucrez ID: {imdb_id}")  # DEBUG
            data = get_movie_data(imdb_id)
            print(f"Date primite pentru {imdb_id}: {data}")  # DEBUG
            if data:
                try:
                    insert_movie_data(conn, data)
                    print(f"Inserat film: {data['title']}")
                except Exception as db_exc:
                    print(f"Eroare la inserare în DB pentru {imdb_id}: {db_exc}")
            time.sleep(1)  # pentru limitare API
        conn.commit()
        print("Toate datele au fost inserate cu succes.")
    except Exception as e:
        print(f"Eroare: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()