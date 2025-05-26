#Libs import
import pandas as pd
from pathlib import Path

#Code
class ExcelHandler:

    def __init__(self):
        pass

    def start_pipeline(self,path_to_read: Path, path_to_write: Path, file_format: str) -> True:

        """
        Função utilizada para dar inicio ao pipeline de transformação de dados. Encapsula \
        a lógica da classe.

        :param path_to_read: Recebe o path no qual os dados se encontram
        :param path_to_write: Recebe o path no qual os dados devem ser salvos
        :param file_format: Recebe uma string indicando o formato no qual os dados devem ser salvos. \
        Deve ser ["csv","parquet"]
        :return: Retorna True para indicar o final do processo
        """

        dataframe = self.extract_excel_data(path=path_to_read)
        transformed_dataframe = self.transform_data(dataframe=dataframe)

        check = self.load_data(path=path_to_write, file_type=file_format, dataframe=transformed_dataframe)

        return check

    def extract_excel_data(self,path: Path) -> pd.DataFrame:
        
        """
        Função utilizada para extrair dados de fonte em excel.

        :param path: Recebe o caminho no qual os dados se encontram
        :return: Retorna um dataframe contendo os dados
        """

        if not isinstance(path, Path):
            raise TypeError("O paramêtro path deve receber um valor de tipo Path")

        dataframe = pd.read_excel(path)

        return dataframe
    
    def transform_data(self,dataframe: pd.DataFrame) -> pd.DataFrame:

        """
        Função utilizada para transofrmação dos dados de uma dataframe

        :param dataframe: Recebe um dataframe contendo dados a serem transformados
        :return: Retorna um dataframe com dados transofrmados
        """

        transformed_dataframe = dataframe[[
            "customer_name","customer_email"
        ]]

        return transformed_dataframe
    
    def load_data(self,path: Path, file_type: str, dataframe: pd.DataFrame) -> True:

        """
        Função utilizada para load dos dados em um determinado caminho.

        :param path: Recebe o caminho no qual os dados devem ser salvos
        :param file_type: Recebe um string indicando o formato do arquivo no qual os dados devem ser \
        salvos. Deve ser ["csv","parquet"]
        :param dataframe: Recebe o dataframe o qual os dados devem ser salvos
        :return: Retorna True para indicar o final do processo
        """

        if file_type == "csv":
            dataframe.to_csv(f"{path}/arquivo.{file_type}")
    
        if file_type == "parquet":
            dataframe.to_parquet(f"{path}/arquivo.{file_type}")

        return True