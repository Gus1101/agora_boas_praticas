#Libs Import
from src.backend.data_handler.data_handler_oop import ExcelHandler
from pathlib import Path

#Settings
excel_handler = ExcelHandler()

#Code
path_read = Path("data/import/fake_data.xlsx")
path_write = Path("data/export/")

excel_handler.start_pipeline(path_to_read=path_read, path_to_write=path_write, file_format="parquet")