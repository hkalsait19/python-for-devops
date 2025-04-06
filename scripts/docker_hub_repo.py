## Fetch Docker Hub Repository Details
## Description: This script fetches details of a Docker Hub repository, such as the number of pulls and stars.

import requests

DOCKER_HUB_API_URL = "https://hub.docker.com/v2/repositories/library/nginx/"

response = requests.get(DOCKER_HUB_API_URL)
if response.status_code == 200:
    repo_data = response.json()
    print(f"Repository: {repo_data['name']}")
    print(f"Pulls: {repo_data['pull_count']}")
    print(f"Stars: {repo_data['star_count']}")
else:
    print(f"Failed to fetch Docker Hub repository details: {response.status_code}")