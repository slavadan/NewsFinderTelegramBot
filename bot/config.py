import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")  # your bot token from .env file
DATABASE = os.getenv("DATABASE_FILE")
