-- sql to create a table users in holberton
-- using enum in table columns

-- Check if the table already exists
IF NOT EXISTS (SELECT * FROM information_schema.tables WHERE table_name = 'users') THEN
    -- Create the table
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    );
END IF;
