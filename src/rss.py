import feedparser
from bs4 import BeautifulSoup
import html
import re
import warnings


class RSSFeedParser:
    def _make_url(self,  bbs_no):
        return f"https://www.knue.ac.kr/rssBbsNtt.do?bbsNo={bbs_no}"

    def parse_entries(self, bbs_no):
        rss_url = self._make_url(bbs_no)
        feed = feedparser.parse(rss_url)
        entries_list = [self._parse_entry(entry)
                        for entry in feed.entries[:10]]
        return entries_list

    def _parse_entry(self, entry):
        entry_info = {}
        clean_summary = self._get_clean_summary(entry.summary)

        entry_info['title'] = entry.title
        entry_info['link'] = entry.link
        entry_info['summary'] = clean_summary
        entry_info['published'] = entry.published

        return entry_info

    def _get_clean_summary(self, summary):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            soup = BeautifulSoup(summary, 'lxml')

        clean_summary = soup.get_text(separator=' ')
        clean_summary = html.unescape(clean_summary)
        clean_summary = self._remove_html_tags(clean_summary)

        if clean_summary.find('"t":') > 0:
            clean_summary = self._clean_hwp_content(clean_summary)

        return ' '.join(clean_summary.split())

    def _remove_html_tags(self, text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def _clean_hwp_content(self, content: str):
        lines = content.split("\n")
        filtered_lines = []

        for line in lines:
            if line.startswith('"t"'):
                filtered_lines.append(line.replace('"t": "', '')[:-1])

        return '\n'.join(filtered_lines)
