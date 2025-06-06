import requests
from config.config import GITHUB_GRAPHQL_URL

def fetch_repos_graphql(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    repos = []
    cursor = None

    for _ in range(10):  # 100 * 10 = 1000
        query = f"""
        {{
          search(query: "stars:>1000", type: REPOSITORY, first: 100{', after: "' + cursor + '" ' if cursor else ''}) {{
            pageInfo {{
              endCursor
              hasNextPage
            }}
            nodes {{
              ... on Repository {{
                nameWithOwner
                stargazerCount
              }}
            }}
          }}
        }}
        """

        response = requests.post(GITHUB_GRAPHQL_URL, headers=headers, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            search_data = data["data"]["search"]
            repos.extend([
                {"nome": r["nameWithOwner"], "estrelas": r["stargazerCount"]}
                for r in search_data["nodes"]
            ])
            if not search_data["pageInfo"]["hasNextPage"]:
                break
            cursor = search_data["pageInfo"]["endCursor"]
        else:
            print(f"Erro GraphQL: {response.status_code}")
            break

    return repos
