# Ingest External API

This folder contains scripts to fetch movie data from the OMDb API and load it into the `movie_ratings_dw` database.

## Files

- `omdb_ingest.py`: Python script to retrieve movie metadata from OMDb.
- `insert_omdb_data.sql`: SQL script to insert the retrieved data into the database.