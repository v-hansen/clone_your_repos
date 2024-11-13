import os
import requests

# Configurações do GitHub
GITHUB_NAME = ""
GITHUB_TOKEN = ""
GITHUB_API_URL = f"https://api.github.com/orgs/{GITHUB_NAME}/repos"
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

# Pasta onde os repositórios serão clonados
CLONE_DIR = "./repositorios"

# Certifique-se de que a pasta existe
if not os.path.exists(CLONE_DIR):
    os.makedirs(CLONE_DIR)

# Função para obter todos os repositórios da organização
def get_repositories():
    repos = []
    page = 1
    while True:
        response = requests.get(f"{GITHUB_API_URL}?per_page=100&page={page}", headers=HEADERS)
        if response.status_code != 200:
            print("Erro ao acessar a API do GitHub. Verifique suas credenciais.")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

# Função para clonar os repositórios
def clone_repositories(repos):
    os.chdir(CLONE_DIR)
    for repo in repos:
        repo_name = repo['name']
        clone_url = repo['clone_url']
        print(f"Clonando {repo_name}...")
        result = os.system(f"git clone {clone_url}")
        if result == 0:
            print(f"{repo_name} clonado com sucesso.")
        else:
            print(f"Falha ao clonar {repo_name}.")

# Executação do script
if __name__ == "__main__":
    repositories = get_repositories()
    if repositories:
        clone_repositories(repositories)
    else:
        print("Nenhum repositório encontrado ou erro ao buscar repositórios.")
