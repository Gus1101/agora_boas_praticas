### Estrutura do projeto
## 📁 Criação de Repositório

Um repositório é um ambiente para armazenar código. Atualmente, usamos Bitbucket e File System, mas a migração para o GitHub está em andamento.

### ✅ Vantagens do Git/GitHub:

- **Versionamento inteligente**: Rastreabilidade e histórico de mudanças.
- **Branches**: Separação de features e correções sem impactar produção.
- **Colaboração**: Múltiplos desenvolvedores trabalhando simultaneamente.

### 🖼️ Diagrama de funcionamento:

![GitHub Simple Arch](/imgs/github_simple_arch.png)



## ⚙️ .env e .gitignore

- **`.env`**: Contém variáveis sensíveis (tokens, senhas etc.).
- **`.gitignore`**: Define arquivos e pastas que **não** devem ser versionados.



## 🐍 Versão do Python

Definir uma versão específica do Python evita problemas de compatibilidade com bibliotecas. Versões antigas podem não suportar pacotes recentes.



## 🧪 Ambiente Virtual

Um ambiente virtual isola bibliotecas do projeto, evitando conflitos entre projetos diferentes.

Analogia: um computador sem ambientes virtuais é como uma casa sem paredes — tudo se mistura!



## 🗂️ Estrutura de Diretórios

Organize seu projeto em pastas com **nomes descritivos** e **responsabilidades separadas**.

```text
.
├── app
│   └── ...
├── src
│   └── backend
│       └── ...
```

![Dir Structure](/imgs/dir_strucuture.png)