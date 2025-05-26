#Libs import
import pandas as pd
from pathlib import Path

#Code
def extract_excel_data(path: Path) -> pd.DataFrame:

    """
    Função utilizada para extrair dados de fonte em excel.

    :param path: Recebe o caminho no qual os dados se encontram
    :return: Retorna um dataframe
    """

    dataframe = pd.read_json(path)

    return dataframe

def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:

    """
    Função utilizada para transofrmação dos dados de uma dataframe

    :param dataframe: Recebe um dataframe contendo dados a serem transformados
    :return: Retorna um dataframe com dados transofrmados
    """

    transformed_dataframe = dataframe[[
        "customer_name","customer_email"
    ]]

    return transformed_dataframe

def load_data(path: Path, file_type: str, dataframe: pd.DataFrame) -> True:

    """
    Função utilizada para load dos dados em um determinado caminho.

    :param path: Recebe o caminho no qual os dados devem ser salvos
    :param file_type: Recebe um string indicando o formato do arquivo no qual os dados devem ser \
    salvos. Deve ser ["csv","parquet"]
    :param dataframe: Recebe o dataframe o qual os dados devem ser salvos
    :return: Retorna True para indicar o final do processo
    """

    if file_type == "csv":
        dataframe.to_csv(path)
    
    if file_type == "parquet":
        dataframe.to_parquet(path)

    return True

if __name__ == "__main__":

    extract_excel_data()
    transform_data()
    load_data()