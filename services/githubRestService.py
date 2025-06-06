import requests

def fetch_repos_rest(token):
    headers = {"Authorization": f"Bearer {token}"}
    per_page = 100
    total_pages = 10  # 100 * 10 = 1000
    all_repos = []

    for page in range(1, total_pages + 1):
        url = f"https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc&per_page={per_page}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = response.json().get("items", [])
            all_repos.extend([
                {"nome": repo["full_name"], "estrelas": repo["stargazers_count"]}
                for repo in items
            ])
        else:
            print(f"Erro REST na página {page}: {response.status_code}")
            break

    return all_repos
