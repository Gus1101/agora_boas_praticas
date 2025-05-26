# Documentação dos Schemas Pandera para Validação de Dados

## Importações
- `pandera.pandas` como `pa`: Biblioteca para validação de dados em DataFrames pandas.
- `pandera.typing.Series`: Tipo anotação para colunas de DataFrame.

## Classes de Modelo (Schemas)

### 1. SchemaExtractExcelDataOut
- Extende `pa.DataFrameModel`.
- Define a estrutura dos dados extraídos do Excel.
- Campos:
  - `customer_name`: Série de strings (nomes dos clientes).
  - `customer_email`: Série de strings (emails dos clientes).
  - `customer_age`: Série de inteiros, com restrição de valor entre 1 e 100 (`pa.Field(ge=1, le=100)`).

### 2. SchemaTransformDataIn
- Herda diretamente de `SchemaExtractExcelDataOut`.
- Representa o formato esperado dos dados na entrada da etapa de transformação.
- Não adiciona campos novos.

### 3. SchemaTransformDataOut
- Extende `pa.DataFrameModel`.
- Define a estrutura dos dados após transformação.
- Campos:
  - `customer_name`: Série de strings.
  - `customer_email`: Série de strings.
- Observação: remove o campo `customer_age` após transformação.

### 4. SchemaLoadDataIn
- Herda diretamente de `SchemaTransformDataOut`.
- Representa o formato esperado dos dados na etapa de carregamento (load).
- Não adiciona campos novos.

## Uso Geral
Esses schemas são utilizados para validação estrutural e de tipos em cada etapa do pipeline de dados, garantindo a qualidade e conformidade dos dados tratados.
