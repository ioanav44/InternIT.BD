
CREATE TABLE IF NOT EXISTS movie_reviews_data (
    review_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20),
    movie_id VARCHAR(20),
    rating INT CHECK (rating >= 1 AND rating <= 10),
    review_text TEXT,
    review_date DATE
);


CREATE TABLE IF NOT EXISTS omdb_metadata (
    movie_id VARCHAR(20) PRIMARY KEY,
    title TEXT,
    year INT,
    genre TEXT,
    director TEXT,
    runtime_minutes INT
);


CREATE TABLE IF NOT EXISTS user_data (
    user_id VARCHAR(20) PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    country VARCHAR(50),
    registration_date DATE
);
