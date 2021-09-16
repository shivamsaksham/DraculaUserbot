from telethon import TelegramClient 
from telethon.sessions import StringSession
import os

string = os.environ['STRING_SESSION']
api_id = os.environ['API_KEY']
api_hash = os.environ['API_HASH']
news_api = os.environ['NEWS_API']

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    
    client.loop.run_until_complete()


# client = TelegramClient(StringSession(string), api_id , api_hash)
