# Check Website Status
# Description: This script checks the status of multiple websites and reports if any are down.

import requests

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsite.com",
    "https://stoplight.io",
    "http://on-prem.stable.stoplight-dev.com",

]

for website in websites:
    try:
        response = requests.get(website)
        print(f"{website} is up and running fine! Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{website} is down! Error: {e}")