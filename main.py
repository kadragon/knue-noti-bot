from src.checker import Checker
from src.llm import request_gpt


if __name__ == '__main__':
    checker = Checker()
    new_datas = checker.update_checker(update_flag=False)

    alert_messages = []

    for n_data in new_datas:
        alert_messages.append(request_gpt(n_data))

    print('\n---\n'.join(alert_messages))
