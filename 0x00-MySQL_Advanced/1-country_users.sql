-- sql to create a table users in holberton
-- using enum in table columns

-- Check if the table already exists
CREATE TABLE users (
	id INTEGER NOT NULL SERIAL PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);
