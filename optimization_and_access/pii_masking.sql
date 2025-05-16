-- Create a view with masked PII data for users
CREATE OR REPLACE VIEW pii_user_data AS
SELECT
    user_id,
    -- Mask age and country, show only gender and registration date
    NULL AS age,
    gender,
    LEFT(country, 2) || '***' AS country,
    registration_date
FROM user_data;