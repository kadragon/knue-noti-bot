"""
This module provides a class to parse RSS feeds from KNUE.
It allows for fetching and cleaning up RSS feed entries, providing a clean and informative summary.
"""

import html
import re
import warnings
import feedparser
from bs4 import BeautifulSoup


class RSSFeedParser:
    """
    A class to parse RSS feed entries and extract useful information.
    """

    def _make_url(self, bbs_no):
        """
        Constructs the URL for the RSS feed based on the given bulletin number.

        Args:
            bbs_no (int): The bulletin number for which the RSS URL is constructed.

        Returns:
            str: The constructed RSS feed URL.
        """
        return f"https://www.knue.ac.kr/rssBbsNtt.do?bbsNo={bbs_no}"

    def parse_entries(self, bbs_no):
        """
        Parses RSS feed entries for the given bulletin number.

        Args:
            bbs_no (int): The bulletin number for which the RSS entries are to be parsed.

        Returns:
            list: A list of parsed RSS entries with cleaned summaries.
        """
        rss_url = self._make_url(bbs_no)
        feed = feedparser.parse(rss_url)
        entries_list = [self._parse_entry(entry)
                        for entry in feed.entries[:10]]
        return entries_list

    def _parse_entry(self, entry):
        """
        Parses an individual RSS entry and extracts relevant information.

        Args:
            entry (feedparser.FeedParserDict): The RSS feed entry to be parsed.

        Returns:
            dict: A dictionary containing the title, link, summary, and published date of the entry.
        """
        entry_info = {}
        clean_summary = self._get_clean_summary(entry.summary)

        entry_info['title'] = entry.title
        entry_info['link'] = entry.link
        entry_info['summary'] = clean_summary
        entry_info['published'] = entry.published

        return entry_info

    def _get_clean_summary(self, summary):
        """
        Cleans the summary of an RSS entry by removing unwanted tags and characters.

        Args:
            summary (str): The summary text to be cleaned.

        Returns:
            str: The cleaned summary text.
        """
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
        """
        Removes HTML tags from the given text.

        Args:
            text (str): The text from which HTML tags need to be removed.

        Returns:
            str: The text without HTML tags.
        """
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def _clean_hwp_content(self, content: str):
        """
        Cleans specific HWP content from the given text.

        Args:
            content (str): The content to be cleaned of HWP-specific lines.

        Returns:
            str: The cleaned content without HWP-specific tags or lines.
        """
        lines = content.split("\n")
        filtered_lines = []

        for line in lines:
            if line.startswith('"t"'):
                filtered_lines.append(line.replace('"t": "', '')[:-1])

        return '\n'.join(filtered_lines)
