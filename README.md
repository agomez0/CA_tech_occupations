#Contributors: Angie, Trinidad, and Jenny

#Goal:
The goal of this project is to prepare and clean data for further evaluation of current and future labor prospects for jobs/careers in the tech industry, with a particular emphasis on data science and analytics.

* The occupations table contains all of the tech-related occupation titles and their occupation code.
* The yearly_stats table contains yearly stats(e.g. annual median income) of tech occupations in California for 2017.

#The repository contains the following files:
* .sql
    -tech_occ_db.sql this file creates the database
* .py
    -app.py to run the ETL code and add data to sql database
    -extract, load, transform - carry out specified functions
* .ipynb
    ook versions that we prototyped the code.

#Resources:
-State_M2017_dl files in csv and excel

#How to use app:
* Insert your mysql database connection settings into the config.py file
* Next, run the tech_occ_db.sql file on mySQL to create the database into which the transformed data will be loaded
* Run the app.py file

#The main source of information is obtained from:
Beaurea of labor statitics
https://www.bls.gov/home.htm

