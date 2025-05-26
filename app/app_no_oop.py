#Libs import
from src.backend.data_handler.data_handler_no_oop import extract_excel_data, transform_data, load_data
from pathlib import Path

#ETL
path_read = Path("data/import/fake_data.xlsx")
path_write = Path("data/export/")

dataframe = extract_excel_data(path=path_read)
transformed_dataframe = transform_data(dataframe=dataframe)
load_data(path=path_write, file_type="csv", dataframe=dataframe)