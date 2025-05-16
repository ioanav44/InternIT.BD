-- Move old reviews to an archive table
CREATE TABLE IF NOT EXISTS archived_movie_reviews AS
SELECT * FROM movie_reviews_data WHERE 1=0;

INSERT INTO archived_movie_reviews
SELECT * FROM movie_reviews_data
WHERE review_date < CURRENT_DATE - INTERVAL '2 years';

DELETE FROM movie_reviews_data
WHERE review_date < CURRENT_DATE - INTERVAL '2 years';