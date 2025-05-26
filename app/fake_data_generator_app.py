#SuperSettings
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

#Libs Import
import pandas as pd
from src.backend.fake_data.fake_data_generator import fake_data_generator

#Generating fake data
fake_data = fake_data_generator(quantity_registers=20)
dataframe = pd.DataFrame(fake_data)
dataframe.to_excel("data/import/fake_data.xlsx")