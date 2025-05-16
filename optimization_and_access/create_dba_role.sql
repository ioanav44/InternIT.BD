-- Create a read-only role for Business Analyst

CREATE ROLE ba_user WITH
    LOGIN
    PASSWORD 'ba_password';

GRANT CONNECT ON DATABASE movie_ratings_dw TO ba_user;
GRANT USAGE ON SCHEMA public TO ba_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ba_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO ba_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ba_user;