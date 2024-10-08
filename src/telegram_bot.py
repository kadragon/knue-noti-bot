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

    def send_message(self, message, link=None):
        """Send a message to the specified Telegram group."""
        if not message:
            print("메시지가 비어 있습니다.")
            return

        try:
            full_message = f"""<a href="{link}">🔗 [게시물 바로가기]</a>

{full_message}

🤖 이 요약은 AI에 의해 작성되었습니다.
"""

            self.bot.send_message(
                self.chat_id,
                full_message,
                parse_mode='HTML'
            )
        except Exception as e:
            print(f"Error sending message: {e}")
