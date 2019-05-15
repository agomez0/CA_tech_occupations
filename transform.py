import pandas as pd
import numpy as np

def transform_data(df):
    
    # Filter by computer related jobs
    tech_df = df[df["OCC_CODE"].str.contains("^15")]
    
    # Renamed columns
    updated_tech_df = tech_df.rename(columns={"H_MEDIAN": "hourly_median", "A_MEDIAN": "annual_median", "OCC_CODE": "occupation_code", "OCC_TITLE": "occupation_title", "H_MEAN": "hourly_mean", "A_MEAN": "annual_mean", "TOT_EMP": "total_employment"})
    
    # Dropped columns with NaN
    updated_tech_df = updated_tech_df.drop(columns=["ANNUAL", "HOURLY"])
    
    print(f'Heres the type of updated_tech_df: {type(updated_tech_df)}')
    
    # Filter extracted data to include only california data
    ca_tech_df = updated_tech_df[updated_tech_df["ST"] == "CA"]

    print(f'Heres the type of ca_tech_df: {type(ca_tech_df)}')

    print(f'The df columns: {ca_tech_df.columns}')

    # create occupation table
    occupations = ca_tech_df[["occupation_code", "occupation_title"]].reset_index(drop=True).copy()

    # create year stats table
    yearly_stats = ca_tech_df[["occupation_code", "hourly_median", "annual_median", "hourly_mean", "annual_mean", "total_employment"]].reset_index(drop=True).copy()

    return (occupations, yearly_stats)