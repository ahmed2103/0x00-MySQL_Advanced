-- MySQL script to create another users table

CREATE TABLE IF NOT EXISTS users (
    id INT not null AUTO_INCREMENT primary key,
    email VARCHAR(255) not null unique,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US'
)
