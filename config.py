from dotenv import load_dotenv
import os

# load .env
load_dotenv()

TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
RECODE_GIST_ID = os.environ.get('RECODE_GIST_ID')
GITHUB_TOKEN = os.environ.get('GIT_HUB_TOKEN')
