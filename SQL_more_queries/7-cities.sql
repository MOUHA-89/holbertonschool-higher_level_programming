-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use newly database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT PRIMARY KEY;
state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES States(id));
