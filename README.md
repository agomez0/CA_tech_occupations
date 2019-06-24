### Contributors: Angie, Trinidad, and Jenny

# California Tech Occupations 2017

## Goal:
The goal of this project is to prepare and clean data for further evaluation of current and future labor prospects for occupations in the tech industry, with a particular emphasis on data science and analytics.

* The occupations table contains all of the tech-related occupation titles and their occupation code.
* The yearly_stats table contains yearly stats(e.g. annual median income) of tech occupations in California for 2017.

## The repository contains the following files:
* .sql
    - tech_occ_db.sql: this file creates the database
* .py
    - app.py to run the ETL code and add data to MySQL database
    - extract, load, transform - carry out specified functions
* .ipynb
    - Jupyter notebook versions in which we prototyped the code

## Resources:
* State_M2017_dl files in csv and excel

## How to use app:
* Copy the `config.example.py` and rename it `config.py`.
* Update your MySQL database connection settings in `config.py`. 
* Next, run the tech_occ_db.sql file on MySQL to create the database into which the transformed data will be loaded.
* Open the terminal in the downloaded repo and run the command `python app.py`

## The main source of information is obtained from:
Beaurea of labor statitics
https://www.bls.gov/home.htm

