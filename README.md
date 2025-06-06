# LAB05 - Comparativo REST vs GraphQL

Este projeto realiza um experimento controlado para comparar as abordagens REST e GraphQL na coleta de dados de repositórios populares do GitHub.

## Objetivo

Comparar o comportamento das APIs REST e GraphQL em aspectos como estrutura da resposta, praticidade de uso e padronização para acesso aos dados.

## Tecnologias

* Python 3.9+
* API REST do GitHub
* API GraphQL do GitHub
* Bibliotecas: requests, dotenv

## Execução

1. Clone o repositório
2. Crie o ambiente virtual e ative:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

1. Crie um arquivo `.env` com o conteúdo:

```env
GITHUB_TOKEN=seu_token_aqui
```

1. Execute o experimento:

```bash
python main.py
```

Os resultados serão salvos em `data/results.json`. Um resumo também é impresso no terminal.
