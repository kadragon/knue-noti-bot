"""
This module provides a TelegramBot class to interact with Telegram API.
It includes methods to initialize the bot and send messages to specific Telegram chat groups.
"""

import telebot
from config import TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID


class TelegramBot:
    """
    A class to interact with Telegram Bot API.
    Provides methods for sending messages to a Telegram group.
    """

    def __init__(self, api_token=TELEGRAM_API_TOKEN):
        """
        Initializes the TelegramBot with the provided API token.

        Args:
            api_token (str): The Telegram API token for the bot.
        """
        self.api_token = api_token
        self.bot = self._initialize_bot()

    def _initialize_bot(self):
        """
        Initializes the TeleBot instance with the provided API token.

        Returns:
            telebot.TeleBot: An instance of the TeleBot class.

        Raises:
            ValueError: If the bot initialization fails.
        """
        try:
            return telebot.TeleBot(self.api_token)
        except Exception as e:
            raise ValueError(f"Failed to initialize Telegram bot: {e}") from e

    def make_full_message(self, message, link):
        """Make Message Using Template"""
        return f"""<a href="{link}">🔗 [게시물 바로가기]</a>

{message}

🤖 이 요약은 AI에 의해 작성되었습니다.
"""

    def send_message(self, message, link=None, target=None):
        """
        Sends a message to the specified Telegram group.

        Args:
            message (str): The message to be sent.
            link (str, optional): A link to be included in the message.
            target (str, optional): The target chat IDs separated by '/'.
        """
        if not message:
            print("메시지가 비어 있습니다.")
            return

        try:
            full_message = self.make_full_message(message=message, link=link)

            for target_id in target.split("/"):
                target_id = int(target_id)
                self.bot.send_message(
                    TELEGRAM_CHAT_ID[target_id],
                    full_message,
                    parse_mode='HTML'
                )
        except ValueError as e:
            print(f"Error sending message: {e}")
            print(full_message)
