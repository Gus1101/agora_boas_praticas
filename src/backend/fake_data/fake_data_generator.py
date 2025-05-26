#Libs import
from faker import Faker
from typing import List, Dict, Any
from random import randint

#Settings
fake = Faker("pt-BR")

#Code
def fake_data_generator(quantity_registers: int) -> List[Dict[str, Any]]:

    """
    Função utilizada para gerar gama de dados falsos.

    :param quantity_registers: Recebe um número inteiro indicando a quantidade de registros a \
    serem gerados
    :return: Retorna uma lista de dicionários contendo os registros gerados.
    """

    data = []

    for _ in range(quantity_registers):
        efem = {
            "customer_name":fake.name(),
            "customer_email":fake.email(),
            "customer_age":randint(1,100),
        }
        data.append(efem)

    return data

if __name__ == "__main__":
    fake_data_generator()