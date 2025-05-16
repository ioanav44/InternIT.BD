-- Check for NULLs in important columns
SELECT COUNT(*) AS null_user_id FROM movie_reviews_data WHERE user_id IS NULL;
SELECT COUNT(*) AS null_movie_id FROM movie_reviews_data WHERE movie_id IS NULL;

-- Check for duplicate reviews
SELECT review_id, COUNT(*) FROM movie_reviews_data GROUP BY review_id HAVING COUNT(*) > 1;