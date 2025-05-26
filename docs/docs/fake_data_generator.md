# Geração de Dados Falsos

Esta função é utilizada para simular dados de clientes, sendo útil em ambientes de desenvolvimento, testes ou demonstrações.

---

## `fake_data_generator(quantity_registers: int) -> List[Dict[str, Any]]`

Gera uma lista de registros com dados fictícios de clientes, incluindo nome, e-mail e idade.

### Parâmetros

| Nome                | Tipo   | Descrição                                               |
|---------------------|--------|----------------------------------------------------------|
| `quantity_registers`| `int`  | Quantidade de registros a serem gerados                 |

### Retorno

Retorna uma lista de dicionários. Cada dicionário representa um cliente simulado com os seguintes campos:

- `customer_name`: Nome completo (ex: João Silva)
- `customer_email`: E-mail fictício (ex: joao.silva@example.com)
- `customer_age`: Idade (número inteiro entre 1 e 100)

### Exemplo de uso

```python
from fake_data_generator import fake_data_generator

dados = fake_data_generator(3)

for registro in dados:
    print(registro)
```

### Saída esperada

```python
[
  {
    'customer_name': 'Ana Paula Vieira',
    'customer_email': 'ana.vieira@example.com',
    'customer_age': 42
  },
  ...
]
```

> ℹ️ **Observação**: A função utiliza a biblioteca [Faker](https://faker.readthedocs.io/) com localização `pt-BR` para gerar nomes e e-mails em português.

---

### Dependências

- `faker`
- `typing`
- `random`
