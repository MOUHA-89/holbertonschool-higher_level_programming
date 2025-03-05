-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,    -- Auto-generated, unique, not null, and primary key
    state_id INT NOT NULL,                        -- Foreign key to the states table, cannot be null
    name VARCHAR(256) NOT NULL,                   -- City name, cannot be null
    FOREIGN KEY (state_id) REFERENCES states(id) -- Foreign key constraint to the states table
);
