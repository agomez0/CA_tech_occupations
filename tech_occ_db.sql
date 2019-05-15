-- Create and use database
DROP DATABASE IF EXISTS tech_occupational_db;
CREATE DATABASE tech_occupational_db;
USE tech_occupational_db;

-- Create tables for raw data to be loaded into
-- DROP TABLE IF EXISTS ccupations;
DROP TABLE IF EXISTS yearly_stats;
DROP TABLE IF EXISTS occupations;

CREATE TABLE occupations (
  occupation_code VARCHAR(16),
  occupation_title VARCHAR(255),
  PRIMARY KEY (occupation_code)
);

CREATE TABLE yearly_stats (
  id INT AUTO_INCREMENT,
  occupation_code VARCHAR(16),
  hourly_median FLOAT,
  annual_median MEDIUMINT,
  hourly_mean FLOAT,
  annual_mean MEDIUMINT,
  total_employment BIGINT,
  PRIMARY KEY (id),
  FOREIGN KEY (occupation_code) REFERENCES occupations(occupation_code)
);
