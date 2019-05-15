import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# PyMySQL 
import pymysql

def load_data_sql(tuple):

    pymysql.install_as_MySQLdb()
    rds_connection_string = "root:root@127.0.0.1:3306/tech_occupational_db"
    engine = create_engine(f'mysql://{rds_connection_string}')
    

    # # Upload table 1 info
    tuple[0].to_sql(name='occupations', con=engine, if_exists='append', index=False)

    # Upload table 2 info
    tuple[1].to_sql(name='yearly_stats', con=engine, if_exists='append', index=False)

    return "upload complete"