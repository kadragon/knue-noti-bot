from dotenv import load_dotenv
import os

# load .env
load_dotenv()

TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID = ['', os.environ.get('TELEGRAM_CHAT_ID_1'), os.environ.get(
    'TELEGRAM_CHAT_ID_2'), os.environ.get('TELEGRAM_CHAT_ID_3')]

RECODE_GIST_ID = os.environ.get('RECODE_GIST_ID')
GIT_HUB_TOKEN = os.environ.get('GIT_HUB_TOKEN')
