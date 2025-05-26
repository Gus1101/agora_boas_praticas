# Documentação do Workflow GitHub Actions: CI

## Nome do Workflow
CI (Continuous Integration)

## Eventos que disparam o workflow
- Push para a branch `main`
- Pull request direcionado à branch `main`

## Jobs

### Job: test
- **Ambiente:** Ubuntu mais recente disponível (`ubuntu-latest`)

### Etapas do Job

1. **Checkout do repositório**
   - Utiliza a ação oficial `actions/checkout@v4`
   - Realiza o checkout do código-fonte para a máquina do runner.

2. **Configuração do Python**
   - Usa a ação `actions/setup-python@v5`
   - Define a versão do Python para 3.13.

3. **Atualização do pip e instalação das dependências**
   - Atualiza o gerenciador de pacotes `pip` para a última versão disponível.
   - Instala o pacote atual (`pip install .`), ou seja, as dependências definidas no projeto.

4. **Execução dos testes**
   - Roda o `pytest` para executar os testes automatizados.
   - Desabilita os warnings para um output mais limpo durante a execução.

## Objetivo do Workflow
Garantir que, a cada mudança feita no código e enviada para a branch principal (main), os testes sejam executados automaticamente para validar a integridade do código e evitar que erros cheguem à produção.
