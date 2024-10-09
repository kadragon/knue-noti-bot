import requests
from config import RECODE_GIST_ID, GIT_HUB_TOKEN


class GistManager:
    BASE_URL = "https://api.github.com/gists/"

    def __init__(self):
        self.gist_id = RECODE_GIST_ID
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {GIT_HUB_TOKEN}"
        }

    def get_gist_content(self):
        response = requests.get(f"{self.BASE_URL}{self.gist_id}")

        if response.status_code == 200:
            gist_data = response.json()
            return {
                filename.split('.')[0]: self.parse_gist_content(
                    file['content'])
                for filename, file in gist_data['files'].items()
            }
        else:
            print(f"Error fetching gist: {
                  response.status_code}, {response.text}")
            return None

    @staticmethod
    def parse_gist_content(content):
        lines = content.strip().split('\n')
        return {
            line.split(',')[0]: {
                'url': line.split(',')[1].strip(),
                'target': line.split(',')[2]
            } for line in lines[1:]
        }

    def update_gist_content(self, files):
        data = {"files": files}
        response = requests.patch(
            f"{self.BASE_URL}{self.gist_id}", headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error updating gist: {
                  response.status_code}, {response.text}")
            return None
