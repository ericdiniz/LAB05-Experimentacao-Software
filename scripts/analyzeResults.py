import json

def analyze_results():
    with open("data/results.json") as f:
        dados = json.load(f)

    print("\nRepositórios via REST:")
    for repo in dados["rest"]:
        print(f"{repo['nome']} - {repo['estrelas']} estrelas")

    print("\nRepositórios via GraphQL:")
    for repo in dados["graphql"]:
        print(f"{repo['nome']} - {repo['estrelas']} estrelas")
