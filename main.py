from src.checker import Checker
from src.llm import request_gpt
from src.telegram_bot import TelegramBot


if __name__ == '__main__':
    telegramBot = TelegramBot()

    updated_data_list = Checker().update_checker(update_flag=True)

    for data in updated_data_list:
        gpt_message = request_gpt(data['entry'])
        telegramBot.send_message(
            gpt_message, data['entry']['link'], data['target'])
