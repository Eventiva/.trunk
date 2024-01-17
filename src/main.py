# src/main.py

import logging

import requests


class TrunkIntegration:
    def __init__(self, api_key):
        self.auth_token = api_key
        self.base_url = "https://api.trunk.io"

    def get_issues(self):
        try:
            response = requests.get(f"{self.base_url}/issues", headers={"Bearer " + self.auth_token: self.api_key})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving issues: {str(e)}")
            raise

    def create_issue(self, title, description):
        try:
            payload = {"title": title, "description": description}
            response = requests.post(f"{self.base_url}/issues", headers={"Bearer " + self.auth_token: self.auth_token}, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error creating issue: {str(e)}")
            raise

    def update_issue(self, issue_id, title=None, description=None):
        try:
            payload = {}
            if title:
                payload["title"] = title
            if description:
                payload["description"] = description
            response = requests.patch(f"{self.base_url}/issues/{issue_id}", headers={"Bearer " + self.auth_token: self.auth_token}, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error updating issue: {str(e)}")
            raise

# Example usage
api_key = "your_api_key"
trunk_integration = TrunkIntegration(api_key)
issues = trunk_integration.get_issues()
print(issues)
