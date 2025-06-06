from services.githubRestService import fetch_repos_rest
from services.githubGraphqlService import fetch_repos_graphql
import json
import os

def run_experiment():
    print("Executando experimento REST e GraphQL...")

    rest_data = fetch_repos_rest()
    graphql_data = fetch_repos_graphql()

    combined = {
        "rest": rest_data,
        "graphql": graphql_data
    }

    os.makedirs("data", exist_ok=True)
    with open("data/results.json", "w") as f:
        json.dump(combined, f, indent=2)

    print("Resultados salvos em data/results.json")

    print("\nRepositórios via REST:")
    for repo in rest_data[:5]:
        print(f"{repo['nome']} - {repo['estrelas']} estrelas - {repo['linguagem']} - {repo['descricao']} - {repo['url']}")

    print("\nRepositórios via GraphQL:")
    for repo in graphql_data[:5]:
        print(f"{repo['nome']} - {repo['estrelas']} estrelas - {repo['linguagem']} - {repo['descricao']} - {repo['url']}")
