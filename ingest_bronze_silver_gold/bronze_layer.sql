-- Bronze layer for reviews
CREATE TABLE IF NOT EXISTS bronze_movie_reviews (
    review_id VARCHAR(50),
    user_id VARCHAR(20),
    movie_id VARCHAR(20),
    rating INT,
    review_text TEXT,
    review_date DATE
);

-- Bronze for user data
CREATE TABLE IF NOT EXISTS bronze_user_data (
    user_id VARCHAR(20),
    age INT,
    gender VARCHAR(10),
    country VARCHAR(50),
    registration_date DATE
);

-- Bronze layer for OMDB metadata
CREATE TABLE IF NOT EXISTS bronze_omdb_metadata (
    imdb_id VARCHAR(20),
    title TEXT,
    year INT,
    rated TEXT,
    released TEXT,
    runtime TEXT,
    genre TEXT,
    director TEXT,
    writer TEXT,
    actors TEXT,
    plot TEXT,
    language TEXT,
    country TEXT,
    awards TEXT,
    poster TEXT,
    metascore TEXT,
    imdb_rating FLOAT,
    imdb_votes TEXT,
    type TEXT,
    dvd TEXT,
    box_office TEXT,
    production TEXT,
    website TEXT
);


-- Normalization: populate dim_user from bronze_user_data
INSERT INTO dim_user (user_id, age, gender, country, registration_date)
SELECT DISTINCT user_id, age, gender, country, registration_date
FROM bronze_user_data
ON CONFLICT (user_id) DO NOTHING;

-- Normalization: populate dim_movie from bronze_omdb_metadata
INSERT INTO dim_movie (movie_id, title, year, genre, director, runtime_minutes)
SELECT DISTINCT imdb_id, title, year, genre, director,
    CAST(NULLIF(regexp_replace(runtime, '[^0-9]', '', 'g'), '') AS INT)
FROM bronze_omdb_metadata
ON CONFLICT (movie_id) DO NOTHING;

-- Normalization: populate dim_date from bronze_movie_reviews
INSERT INTO dim_date (date_id, year, month, day)
SELECT DISTINCT review_date,
    EXTRACT(YEAR FROM review_date),
    EXTRACT(MONTH FROM review_date),
    EXTRACT(DAY FROM review_date)
FROM bronze_movie_reviews
WHERE review_date IS NOT NULL
ON CONFLICT (date_id) DO NOTHING;

-- Normalization: populate fact_movie_review from bronze_movie_reviews
INSERT INTO fact_movie_review (review_id, user_id, movie_id, date_id, rating, review_text)
SELECT review_id, user_id, movie_id, review_date, rating, review_text
FROM bronze_movie_reviews
ON CONFLICT (review_id) DO NOTHING;