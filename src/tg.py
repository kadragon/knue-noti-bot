import telebot
import os
from dotenv import load_dotenv
from telebot.types import LinkPreviewOptions

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


class Tg:
    def __init__(self):
        self.bot = telebot.TeleBot(API_TOKEN)

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
            CHAT_ID, message, link_preview_options=self._make_link_options(link))
