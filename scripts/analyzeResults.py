import json
import matplotlib.pyplot as plt
import os

def carregar_dados():
    with open("data/results.json", "r") as f:
        return json.load(f)

def gerar_grafico_estrelas(dados):
    rest_nomes = [repo["nome"] for repo in dados["rest"][:10]]
    rest_estrelas = [repo["estrelas"] for repo in dados["rest"][:10]]

    graphql_nomes = [repo["nome"] for repo in dados["graphql"][:10]]
    graphql_estrelas = [repo["estrelas"] for repo in dados["graphql"][:10]]

    # REST
    plt.figure(figsize=(12, 6))
    plt.barh(rest_nomes[::-1], rest_estrelas[::-1])
    plt.title("Top 10 repositórios por estrelas - REST")
    plt.xlabel("Estrelas")
    plt.tight_layout()
    os.makedirs("charts", exist_ok=True)
    plt.savefig("charts/rest_top10.png")
    plt.close()

    # GraphQL
    plt.figure(figsize=(12, 6))
    plt.barh(graphql_nomes[::-1], graphql_estrelas[::-1])
    plt.title("Top 10 repositórios por estrelas - GraphQL")
    plt.xlabel("Estrelas")
    plt.tight_layout()
    plt.savefig("charts/graphql_top10.png")
    plt.close()

def analyze_results():
    print("📊 Analisando resultados e gerando gráficos...")
    dados = carregar_dados()
    gerar_grafico_estrelas(dados)
    print("✅ Gráficos salvos em charts/")

if __name__ == "__main__":
    analyze_results()
