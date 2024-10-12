from src.gist import GistManager
from src.rss import RSSFeedParser
from src.checker import Checker
from src.llm import request_gpt
from src.telegram_bot import TelegramBot


if __name__ == '__main__':
    # Instantiate dependencies
    telegramBot = TelegramBot()
    gist_manager = GistManager()
    rss_parser = RSSFeedParser()

    # Inject dependencies into Checker
    checker = Checker(gist_manager=gist_manager, rss_parser=rss_parser)

    # Use the checker
    new_entries = checker.update_checker(update_flag=True)

    for entry in new_entries:
        gpt_message = request_gpt(entry['entry'])
        telegramBot.send_message(
            gpt_message, entry['entry']['link'], entry['target'])
