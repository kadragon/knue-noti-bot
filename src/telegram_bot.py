import telebot
from config import TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID


class TelegramBot:
    def __init__(self, api_token=TELEGRAM_API_TOKEN, chat_id=TELEGRAM_CHAT_ID):
        self.api_token = api_token
        self.chat_id = chat_id
        self.bot = self._initialize_bot()

    def _initialize_bot(self):
        try:
            return telebot.TeleBot(self.api_token)
        except Exception as e:
            raise ValueError(f"Failed to initialize Telegram bot: {e}")

    def send_message_to_group(self, message, link=None):
        """Send a message to the specified Telegram group."""
        try:
            # Properly format the message with the link at the bottom if it exists
            if link:
                full_message = (
                    f"""{message}

<a href="{link}">🔗 바로가기</a>

🤖 이 요약은 AI에 의해 작성되었습니다.
"""
                )
            else:
                full_message = message

            self.bot.send_message(
                self.chat_id,
                full_message,
                parse_mode='HTML'
            )
        except Exception as e:
            print(f"Error sending message to Telegram group: {e}")
