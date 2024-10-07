import requests
from config import RECODE_GIST_ID, GIT_HUB_TOKEN


def get_gist_content():
    url = f"https://api.github.com/gists/{RECODE_GIST_ID}"
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


def update_gist_content(files):
    url = f"https://api.github.com/gists/{RECODE_GIST_ID}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GIT_HUB_TOKEN}"
    }
    data = {
        "files": files
    }
    response = requests.patch(url, headers=headers,
                              json=data)  # data를 json으로 변경

    print(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")  # 에러 메시지 출력
        return None  # None으로 명시적으로 반환
