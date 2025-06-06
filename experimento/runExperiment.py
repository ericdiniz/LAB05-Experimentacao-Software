from services.githubRestService import fetch_repos_rest
from services.githubGraphqlService import fetch_repos_graphql
from config.config import GITHUB_TOKEN
import json
import os

def run_experiment():
    print("Executando experimento REST e GraphQL...")

    rest_data = fetch_repos_rest(GITHUB_TOKEN)
    graphql_data = fetch_repos_graphql(GITHUB_TOKEN)

    combined = {
        "rest": rest_data,
        "graphql": graphql_data
    }

    os.makedirs("data", exist_ok=True)
    with open("data/results.json", "w") as f:
        json.dump(combined, f, indent=2)

    print("Resultados salvos em data/results.json")
