import feedparser
from bs4 import BeautifulSoup
import html
import re


class RSSFeedParser:
    def __init__(self, bbs_no):
        self.rss_url = self._make_url(bbs_no)
        self.feed = feedparser.parse(self.rss_url)

    def _make_url(self,  bbs_no):
        return f"https://www.knue.ac.kr/rssBbsNtt.do?bbsNo={bbs_no}"

    def remove_html_tags(self, text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def display_feed_info(self):
        print(f"피드 제목: {self.feed.feed.title}")
        print(f"피드 설명: {self.feed.feed.description}")

    def parse_entries(self):
        entries_list = []  # 항목 정보를 저장할 리스트
        entry = self.feed.entries[:10]

        for entry in self.feed.entries:
            entry_info = {}  # 각 항목 정보를 저장할 딕셔너리

            # HTML 태그 제거 및 텍스트 정리
            soup = BeautifulSoup(entry.summary, 'html.parser')
            clean_summary = soup.get_text(separator=' ')
            clean_summary = html.unescape(clean_summary)
            clean_summary = self.remove_html_tags(clean_summary)

            # 한글 파일 복사 붙여넣기 방지
            if clean_summary.find('"t":') > 0:
                split_clean_summary = clean_summary.split("\n")
                filtered_text = []

                for txt in split_clean_summary:
                    if txt.startswith('"t"'):
                        filtered_text.append(txt.replace('"t": "', '')[:-1])

                clean_summary = '\n'.join(filtered_text)

            clean_summary = ' '.join(clean_summary.split())

            entry_info['title'] = entry.title
            entry_info['link'] = entry.link
            entry_info['summary'] = clean_summary
            entry_info['published'] = entry.published

            entries_list.append(entry_info)  # 리스트에 항목 정보 추가

        return entries_list  # 항목 정보 리스트 반환
