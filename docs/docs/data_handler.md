# Classe `ExcelHandler`

A classe `ExcelHandler` encapsula o pipeline de leitura, transformação e gravação de dados a partir de arquivos Excel.

---

## `ExcelHandler`

Classe para manipulação de dados utilizando Pandas e validação com Pandera.

### Métodos

---

### `start_pipeline(path_to_read: Path, path_to_write: Path, file_format: str) -> True`

Inicia a pipeline de transformação de dados.

#### Parâmetros

| Nome             | Tipo   | Descrição                                                   |
|------------------|--------|--------------------------------------------------------------|
| `path_to_read`   | `Path` | Caminho de leitura do arquivo Excel                          |
| `path_to_write`  | `Path` | Caminho onde o arquivo transformado será salvo              |
| `file_format`    | `str`  | Formato de saída do arquivo: `"csv"` ou `"parquet"`         |

#### Retorno

- `True` ao final do processo, indicando sucesso

---

### `extract_excel_data(path: Path) -> DataFrame[SchemaExtractExcelDataOut]`

Extrai os dados de um arquivo Excel.

#### Parâmetros

| Nome   | Tipo   | Descrição                          |
|--------|--------|-------------------------------------|
| `path` | `Path` | Caminho para o arquivo Excel       |

#### Retorno

- Um `DataFrame` validado com o schema `SchemaExtractExcelDataOut`

---

### `transform_data(dataframe: DataFrame[SchemaTransformDataIn]) -> DataFrame[SchemaTransformDataOut]`

Transforma os dados extraídos.

#### Parâmetros

| Nome        | Tipo                             | Descrição                              |
|-------------|----------------------------------|-----------------------------------------|
| `dataframe` | `DataFrame[SchemaTransformDataIn]` | DataFrame com os dados brutos         |

#### Retorno

- Um `DataFrame` validado com o schema `SchemaTransformDataOut` contendo apenas `customer_name` e `customer_email`

---

### `load_data(path: Path, file_type: str, dataframe: DataFrame[SchemaLoadDataIn]) -> True`

Salva os dados transformados em formato CSV ou Parquet.

#### Parâmetros

| Nome        | Tipo                             | Descrição                                              |
|-------------|----------------------------------|---------------------------------------------------------|
| `path`      | `Path`                           | Caminho onde o arquivo deve ser salvo                   |
| `file_type` | `str`                            | Formato de arquivo (`"csv"` ou `"parquet"`)            |
| `dataframe` | `DataFrame[SchemaLoadDataIn]`    | DataFrame validado a ser salvo                         |

#### Retorno

- `True` ao concluir a escrita do arquivo

---

## Dependências

- `pandas`
- `pandera`
- `pathlib`
- `typing`

---

## Observações

- Toda a validação de schema é feita com `pandera` e tipagem forte com `DataFrame[SchemaX]`
- A classe assume que os schemas foram definidos previamente em `models.models_data_handler_oop`
