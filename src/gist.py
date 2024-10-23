"""
This module provides a GistManager class to manage GitHub Gists.
It includes methods to retrieve and update gist content.
"""

import requests
from config import RECODE_GIST_ID, GIT_HUB_TOKEN


class GistManager:
    """
    A class to manage GitHub Gists.
    Provides methods to retrieve and update gist content.
    """
    BASE_URL = "https://api.github.com/gists/"

    def __init__(self):
        """
        Initializes GistManager with the given Gist ID and GitHub token.
        """
        self.gist_id = RECODE_GIST_ID
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {GIT_HUB_TOKEN}"
        }

    @staticmethod
    def parse_gist_content(content):
        """
        Parses the content of a gist file.

        Args:
            content (str): The content of the gist file.

        Returns:
            dict: A dictionary representing the parsed gist content.
        """
        lines = content.strip().split('\n')
        return {
            line.split(',')[0]: {
                'url': line.split(',')[1].strip(),
                'target': line.split(',')[2]
            } for line in lines[1:]
        }

    def get_gist_content(self):
        """
        Retrieves the content of the specified gist.

        Returns:
            dict: A dictionary with filenames as keys and parsed content as values.
        """
        response = requests.get(f"{self.BASE_URL}{self.gist_id}", timeout=5)

        if response.status_code == 200:
            gist_data = response.json()
            return {
                filename.split('.')[0]: self.parse_gist_content(
                    file['content'])
                for filename, file in gist_data['files'].items()
            }

        print(f"Error fetching gist: {response.status_code}, {response.text}")
        return None

    def update_gist_content(self, files):
        """
        Updates the content of the specified gist.

        Args:
            files (dict): A dictionary with filenames as keys and their new content as values.

        Returns:
            dict or None: The updated gist data if the update is successful, otherwise None.
        """
        data = {"files": files}
        response = requests.patch(
            f"{self.BASE_URL}{self.gist_id}", headers=self.headers, json=data, timeout=5)

        if response.status_code == 200:
            return response.json()

        print(f"Error updating gist: {response.status_code}, {response.text}")
        return None
