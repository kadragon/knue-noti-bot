import requests
import json


def get_gist_content(gist_id):
    url = f"https://api.github.com/gists/{gist_id}"
    response = requests.get(url)

    if response.status_code == 200:
        gist_data = response.json()
        for file in gist_data['files'].values():
            content = file['content']
            return parse_gist_content(content)
    else:
        return None


def parse_gist_content(content):
    lines = content.strip().split('\n')
    data = {}
    for line in lines:
        key, url = line.split(',')
        data[key] = url.strip()
    return data


# if __name__ == '__main__':
#     # Gist ID를 여기에 입력하세요
#     gist_id = "09b40531d20c143009eedf15b66b0950"

#     content = get_gist_content(gist_id)
#     if content:
#         parsed_data = parse_gist_content(content)
#         print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
#     else:
#         print("Gist를 불러오는 데 실패했습니다.")
