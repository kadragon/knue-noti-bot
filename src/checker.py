"""Module for checking and updating RSS feed entries using GistManager."""

from src.gist import GistManager
from src.rss import RSSFeedParser


class Checker:
    """Class to check and update RSS feed entries using GistManager."""

    def __init__(self,
                 gist_manager: GistManager,
                 rss_parser: RSSFeedParser) -> None:
        self.gist_manager = gist_manager
        self.rss_parser = rss_parser
        self.gist_data = {}

    def load_gist_data(self):
        """Load gist data from the GistManager."""
        self.gist_data = self.gist_manager.get_gist_content()

    def check_new_entries(self, idx, latest_article_url):
        """Check for new RSS feed entries that are not the latest article."""
        entries = self.rss_parser.parse_entries(idx)
        new_entries = []

        for entry in entries:
            if entry['link'] != latest_article_url:
                new_entries.append(entry)
            else:
                break
        return new_entries

    def generate_updated_content(self, recode, new_entries):
        """Generate updated content for the gist based on new entries."""
        updated_content = []

        for idx in recode.keys():
            latest_article_url = (
                new_entries[idx][0]['link']
                if idx in new_entries
                else recode[idx]['url']
            )
            target = recode[idx]['target']
            updated_content.append(
                f"{idx},{latest_article_url},{target}"
            )
        return updated_content

    def update_checker(self, update_flag: bool = False) -> list:
        """Update the gist content with new RSS feed entries if there are any."""
        base_text = "bbs_no,latest_article_url,notification_target"

        self.load_gist_data()
        new_entries = []
        updated_data = {}
        is_data_updated = False

        for site_id, recode in self.gist_data.items():
            gist_filename = f'{site_id}.csv'
            site_new_entries, site_new_entries_list = self.process_site_entries(
                recode)

            if site_new_entries_list:
                new_entries.extend(site_new_entries_list)
                is_data_updated = True

            updated_content = self.generate_updated_content(
                recode, site_new_entries)

            updated_data[gist_filename] = {
                'content': f"{base_text}\n{'\n'.join(updated_content)}"
            }

        if update_flag and is_data_updated:
            self.gist_manager.update_gist_content(updated_data)

        return new_entries

    def process_site_entries(self, recode):
        """Process entries for a single site."""
        site_new_entries = {}
        site_new_entries_list = []

        for idx in recode.keys():
            latest_article_url = recode[idx]['url']
            target = recode[idx]['target']
            entries = self.check_new_entries(idx, latest_article_url)

            if entries:
                site_new_entries[idx] = entries
                for entry in entries:
                    site_new_entries_list.append(
                        {'entry': entry, 'target': target})

        return site_new_entries, site_new_entries_list
