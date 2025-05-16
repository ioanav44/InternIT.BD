-- This view provides a list of the top 10 movies in the last 30 days.

CREATE OR REPLACE VIEW gold_top10_movies_last_30_days AS
SELECT
    m.title,
    AVG(f.rating) AS avg_rating,
    COUNT(f.review_id) AS review_count
FROM fact_movie_review f
JOIN dim_movie m ON f.movie_id = m.movie_id
WHERE f.date_id >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY m.title
ORDER BY avg_rating DESC
LIMIT 10;

-- This view provides a list of the top movies based by genre

CREATE OR REPLACE VIEW gold_rating_trend_by_genre AS
SELECT
    d.year,
    m.genre,
    AVG(f.rating) AS avg_rating
FROM fact_movie_review f
JOIN dim_movie m ON f.movie_id = m.movie_id
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, m.genre
ORDER BY d.year, m.genre;

--Average score by country
-- This view calculates the average rating and review count for movies by country.

CREATE OR REPLACE VIEW gold_avg_score_by_country AS
SELECT
    u.country,
    AVG(f.rating) AS avg_rating,
    COUNT(f.review_id) AS review_count
FROM fact_movie_review f
JOIN dim_user u ON f.user_id = u.user_id
GROUP BY u.country
ORDER BY avg_rating DESC;