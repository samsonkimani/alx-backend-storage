-- sql to create a table users in holberton
-- using enum in table columns

CREATE TABLE IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE,
	name VARCHAR(255),
	country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);	
