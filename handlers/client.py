from telethon import TelegramClient 
import os

api_id = os.environ['API_KEY']
api_hash = os.environ['API_HASH']
news_api = os.environ['NEWS_API']
client = TelegramClient('devil', api_id , api_hash)