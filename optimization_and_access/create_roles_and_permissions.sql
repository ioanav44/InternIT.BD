-- Create a user for client and give permissions for data access
CREATE ROLE client_user WITH
    LOGIN
    PASSWORD 'client_password';

GRANT CONNECT ON DATABASE movie_ratings_dw TO client_user;
GRANT USAGE ON SCHEMA public TO client_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO client_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO client_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO client_user;