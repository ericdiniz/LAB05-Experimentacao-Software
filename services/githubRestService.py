import requests
from config.config import GITHUB_TOKEN

def fetch_repos_rest():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.mercy-preview+json"  # para acessar os "topics"
    }

    all_repos = []
    for page in range(1, 11):  # 1000 / 100
        url = f"https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc&per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro na REST API: {response.status_code}")
            break

        for repo in response.json().get("items", []):
            all_repos.append({
                "nome": repo["full_name"],
                "estrelas": repo["stargazers_count"],
                "linguagem": repo["language"],
                "descricao": repo["description"],
                "url": repo["html_url"],
                "forks": repo["forks_count"],
                "criado_em": repo["created_at"],
                "atualizado_em": repo["updated_at"],
                "tamanho": repo["size"],
                "topicos": repo.get("topics", []),
                "watchers": repo["watchers_count"],
            })

    return all_repos
