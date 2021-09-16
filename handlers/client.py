from telethon import TelegramClient 
from telethon.sessions import StringSession
import os

string = os.environ['STRING_SESSION']
api_id = os.environ['API_KEY']
api_hash = os.environ['API_HASH']
news_api = os.environ['NEWS_API']

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    ...  # use the client

    
    string = client.session.save()

# Note that it's also possible to save any other session type
# as a string by using ``StringSession.save(session_instance)``:
# client = TelegramClient('sqlite-session', api_id, api_hash)
# string = StringSession.save(client.session)
# client = TelegramClient(StringSession(string), api_id , api_hash)
