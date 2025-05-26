#Libs Import
import pytest

from src.backend.data_handler.data_handler_oop import ExcelHandler

#Tests
def test_extract_data_excel_path_is_type_path():

    """
    Função para testar se o path indicado no método extract_data_excel é do tipo Path.
    """

    #Arrange
    excel_handler = ExcelHandler()
    path_read = "string"

    #Act
    with pytest.raises(TypeError):
        excel_handler.extract_excel_data(path=path_read)

    #Assert
    assert "O paramêtro path deve receber um valor de tipo Path"