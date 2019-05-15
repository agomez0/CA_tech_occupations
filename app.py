import extract
import transform
import load_data

if __name__ == "__main__":
    extract_dataframe = extract.extract_data("Resources/state_M2017_dl.xlsx")
    transform_data = transform.transform_data(extract_dataframe)
    load_data_to_sql = load_data.load_data_sql(transform_data)
