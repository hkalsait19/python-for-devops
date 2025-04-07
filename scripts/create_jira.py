# # This code sample uses the 'requests' library:
# # http://docs.python-requests.org


import requests
from requests.auth import HTTPBasicAuth

# Jira credentials
JIRA_BASE_URL = "https://yourblahblah.atlassian.net"  # Replace with your Jira domain
JIRA_API_ENDPOINT = f"{JIRA_BASE_URL}/rest/api/2/issue"
USERNAME = "your user name"  # Replace with your Jira email
API_TOKEN = "yourtoken JIRA token"

# Define the payload (issue details)
payload = {
    "fields": {
        "project": {
            "key": "SCRUM"  # Replace with your Jira project key
        },
        "summary": "Request: <> - Upgrade Workspace to <> (Due:)",
        "description": "This is a Request for Workspace Upgrade: Upgrade Workspace to <> using on-call tool.", 
        #"summary": "Sample Issue Created via API",  # Short title of the issue
        ##"description": "This is a test issue created using the Jira REST API.",  # Detailed description
        "labels": ["workspace-upgrade" , "on-call-tool", "request"],
        "issuetype": {
            "name": "Task"  # Replace with the issue type (e.g., Bug, Task, Story)
        }
    }
}

# Make the API request
response = requests.post(
    JIRA_API_ENDPOINT,
    json=payload,  # Pass the payload as JSON
    auth=HTTPBasicAuth(USERNAME, API_TOKEN),
    headers={"Content-Type": "application/json"}
)

# Handle the response
if response.status_code == 201:
    print("Issue created successfully!")
    print("Response:", response.json())
else:
    print(f"Failed to create issue. HTTP Status Code: {response.status_code}")
    print("Response:", response.json())