-- create database
CREATE DATABASE hbtn_0d_usa;
-- Use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE,AUTO_GENERATED, PRIMARY KEY, name VARCHAR(256) NOT NULL);
