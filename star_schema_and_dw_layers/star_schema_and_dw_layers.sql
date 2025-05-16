-- Dimension: Movie
CREATE TABLE IF NOT EXISTS dim_movie (
    movie_id VARCHAR(20) PRIMARY KEY,
    title TEXT,
    year INT,
    genre TEXT,
    director TEXT,
    runtime_minutes INT
);

-- Dimension: User
CREATE TABLE IF NOT EXISTS dim_user (
    user_id VARCHAR(20) PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    country VARCHAR(50),
    registration_date DATE
);

-- Dimension: Date
CREATE TABLE IF NOT EXISTS dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- Fact Table: Movie Review
CREATE TABLE IF NOT EXISTS fact_movie_review (
    review_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20) REFERENCES dim_user(user_id),
    movie_id VARCHAR(20) REFERENCES dim_movie(movie_id),
    date_id DATE REFERENCES dim_date(date_id),
    rating INT,
    review_text TEXT
);