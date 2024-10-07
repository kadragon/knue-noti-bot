from src.gist import *
from src.rss import RSSFeedParser


class Checker:
    def __init__(self) -> None:
        self.gist_data = get_gist_content()
        self.update_data = {}

    def update_checker(self, update_flag: bool = False) -> list:
        new_data = []

        for site_id in self.gist_data.keys():
            gist_filename = f'{site_id}.csv'
            self.update_data[gist_filename] = {'content': ''}

            recode = self.gist_data[site_id]

            for idx in recode.keys():
                entries = RSSFeedParser(idx).parse_entries()

                self.update_data[gist_filename]['content'] += f'{
                    idx},{entries[0]['link']}\n'

                for entry in entries:
                    if entry['link'] != recode[idx]:
                        new_data.append(entry)
                    else:
                        break
        if update_flag:
            update_gist_content(self.update_data)

        return new_data
