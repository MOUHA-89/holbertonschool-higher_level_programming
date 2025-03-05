-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use newly database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT PRIMARY KEY; -- auto generated unique end not null
state_id INT NOT NULL, -- not null 
name VARCHAR(256) NOT NULL, -- name not null
FOREIGN KEY (state_id) REFERENCES States(id) -- FOREIGN KEY that references to id of the states table
); 