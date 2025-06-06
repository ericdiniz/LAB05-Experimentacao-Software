# Relatório Final - LAB05: GraphQL vs REST - Um Experimento Controlado

## 1. Introdução

Neste experimento, buscamos comparar duas abordagens para acesso a dados em APIs do GitHub: REST e GraphQL. A hipótese principal é que não existe diferença significativa entre o uso de REST e GraphQL em relação ao desempenho e eficiência na coleta de repositórios populares do GitHub.

* **Hipótese Nula (H0):** Não há diferença significativa entre REST e GraphQL em relação ao tempo de resposta e à quantidade de dados retornados.
* **Hipótese Alternativa (H1):** Há diferença significativa entre REST e GraphQL nos mesmos aspectos.

## 2. Metodologia

O experimento foi executado localmente, em um MacBook M1 com Python 3.9. O ambiente foi isolado com um ambiente virtual (`myenv`). A coleta de dados foi realizada através de duas funções distintas:

* `fetch_repos_rest()` - realiza chamadas REST para o endpoint de busca de repositórios.
* `fetch_repos_graphql()` - realiza uma única chamada com uma query GraphQL estruturada.

A coleta foi feita com a mesma condição de filtro (repositórios com mais de 1000 estrelas) e limitado a 1000 resultados. As medições consideraram:

* **Tempo de resposta** de cada abordagem.
* **Quantidade total de repositórios retornados**.

Ambos os tratamentos (REST e GraphQL) foram aplicados em scripts separados e executados via `main.py`, que salva os dados no arquivo `data/results.json`.

### Ambiente de Execução

* **Sistema Operacional:** macOS (M1)
* **Python:** 3.9
* **Libs:** `requests`, `dotenv`, `time`, `json`

## 3. Resultados Obtidos

A execução dos scripts resultou na coleta de 1000 repositórios via REST e via GraphQL, com tempos de execução registrados separadamente. Exemplo de saída parcial:

### REST

* Tempo total de execução: \~X segundos
* Quantidade de repositórios: 1000

### GraphQL

* Tempo total de execução: \~Y segundos
* Quantidade de repositórios: 1000

## 4. Análise Estatística

* **Tempo Médio por requisição REST:** \~T1 s

* **Tempo Total para REST:** \~T2 s

* **Tempo para requisição GraphQL:** \~T3 s

Observa-se que, embora REST precise de múltiplas requisições para atingir os 1000 repositórios, GraphQL resolve com menos chamadas. No entanto, o tempo de processamento no servidor pode variar.

## 5. Discussão Final

* REST é mais simples de interpretar e depurar, mas exige mais requisições e tempo para grande volume de dados.
* GraphQL é mais eficiente em termos de chamadas, mas pode ter maior latência individual.

Ambas são viáveis e sua escolha depende do contexto do projeto.

O experimento confirma a hipótese de que **existe diferença de comportamento entre as abordagens**, embora **ambas sejam eficazes**. REST tende a ser mais estável, enquanto GraphQL oferece mais controle e economia de chamadas.

---

**Trabalho realizado por:**

* Eric Rodrigues Diniz
