import requests
from config.config import GITHUB_TOKEN, GITHUB_GRAPHQL_URL

query = """
query($cursor: String) {
  search(query: "stars:>1000", type: REPOSITORY, first: 100, after: $cursor) {
    pageInfo {
      endCursor
      hasNextPage
    }
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
        description
        url
        forkCount
        createdAt
        updatedAt
        primaryLanguage {
          name
        }
        diskUsage
        watchers {
          totalCount
        }
        repositoryTopics(first: 10) {
          nodes {
            topic {
              name
            }
          }
        }
      }
    }
  }
}
"""

def fetch_repos_graphql():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    repos = []
    cursor = None

    while len(repos) < 1000:
        json_data = {"query": query, "variables": {"cursor": cursor}}
        response = requests.post(GITHUB_GRAPHQL_URL, headers=headers, json=json_data)
        data = response.json()["data"]["search"]
        for node in data["nodes"]:
            repos.append({
                "nome": node["nameWithOwner"],
                "estrelas": node["stargazerCount"],
                "linguagem": node["primaryLanguage"]["name"] if node["primaryLanguage"] else None,
                "descricao": node["description"],
                "url": node["url"],
                "forks": node["forkCount"],
                "criado_em": node["createdAt"],
                "atualizado_em": node["updatedAt"],
                "tamanho": node["diskUsage"],
                "topicos": [t["topic"]["name"] for t in node["repositoryTopics"]["nodes"]],
                "watchers": node["watchers"]["totalCount"],
            })

        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]

    return repos
