from src.checker import Checker
from src.llm import request_gpt
from src.tg import Tg


if __name__ == '__main__':
    checker = Checker()
    tg = Tg()
    new_data_list = checker.update_checker(update_flag=False)

    alert_messages = []

    for data_item in new_data_list:
        gpt_message = request_gpt(data_item)

        tg.send_message_to_group(gpt_message, data_item['link'])

        break
