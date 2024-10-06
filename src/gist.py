import requests
import json


def get_gist_content(gist_id):
    url = f"https://api.github.com/gists/{gist_id}"
    response = requests.get(url)

    if response.status_code == 200:
        gist_data = response.json()
        content_map = {}
        for filename, file in gist_data['files'].items():
            filename = filename.split('.')[0]
            content = file['content']
            content_map[filename] = parse_gist_content(content)
        return content_map
    else:
        return None


def parse_gist_content(content):
    lines = content.strip().split('\n')
    data = {}
    for line in lines:
        key, url = line.split(',')
        data[key] = url.strip()
    return data


def update_gist_content(github_token, gist_id, files):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}"
    }
    data = {
        "files": {files}
    }
    response = requests.patch(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return None
