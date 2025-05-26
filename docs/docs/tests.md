# Documentação do teste: `test_extract_data_excel_path_is_type_path`

## Descrição
Função para testar se o parâmetro `path` indicado no método `extract_excel_data` da classe `ExcelHandler` é do tipo `Path`.

## Objetivo do teste
Garantir que o método `extract_excel_data` lance um erro do tipo `TypeError` quando receber um argumento que não seja uma instância da classe `Path`.

## Estrutura do teste (AAA)

- **Arrange (Preparação):**
  - Instancia a classe `ExcelHandler`.
  - Define um valor incorreto para `path` (uma string em vez de um objeto `Path`).

- **Act (Ação):**
  - Executa o método `extract_excel_data` com o parâmetro incorreto, esperando que uma exceção `TypeError` seja lançada.

- **Assert (Verificação):**
  - Verifica se a exceção foi realmente lançada.
  - Confirma que a mensagem de erro está adequada ("O paramêtro path deve receber um valor de tipo Path").

## Importante
Este teste valida a tipagem do parâmetro de entrada para garantir maior robustez e evitar falhas silenciosas em tempo de execução.
