import src.gist as gist
from src.rss import RSSFeedParser


class Checker:
    def __init__(self) -> None:
        self.gist_data = gist.get_gist_content()

    def update_checker(self, update_flag: bool = False) -> list:
        parser = RSSFeedParser()

        new_entries = []
        updated_data = {}

        is_data_updated = False

        for site_id in self.gist_data.keys():
            gist_filename = f'{site_id}.csv'
            updated_content = []

            recode = self.gist_data[site_id]

            for idx in recode.keys():
                latest_article_url = self.gist_data[site_id][idx]['url']
                target = self.gist_data[site_id][idx]['target']

                entries = parser.parse_entries(idx)

                updated_content.append(f'{idx},{entries[0]['link']},{target}')

                for entry in entries:
                    if entry['link'] != latest_article_url:
                        new_entries.append({'entry': entry, 'target': target})
                        is_data_updated = True
                    else:
                        break

            updated_data[gist_filename] = {
                'content': f"""bbs_no,latest_article_url,notification_target\n{'\n'.join(updated_content)}"""}

        if update_flag and is_data_updated:
            gist.update_gist_content(updated_data)

        return new_entries
