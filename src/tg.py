import telebot
from telebot.types import LinkPreviewOptions
from config import TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID


class Tg:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

    def _make_link_options(self, link):
        return LinkPreviewOptions(
            is_disabled=False,
            url=link,
            prefer_small_media=True,
            prefer_large_media=False,
            show_above_text=True
        )

    def send_message_to_group(self, message, link):
        self.bot.send_message(
            TELEGRAM_CHAT_ID, message, parse_mode='HTML', link_preview_options=self._make_link_options(link))
