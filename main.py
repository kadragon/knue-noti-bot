# from src.telegram_bot import bot


# def main():
#     bot.polling()


# if __name__ == '__main__':
#     main()
from src.gist import *
from src.rss import RSSFeedParser
from config import RECODE_GIST_ID


if __name__ == '__main__':
    recode = get_gist_content(RECODE_GIST_ID)

    for idx in recode.keys():
        parser = RSSFeedParser(idx)
        last_entry = parser.parse_last_entry()

        if last_entry['link'] != recode[idx]:
            print(idx, last_entry['link'])
