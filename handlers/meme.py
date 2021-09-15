from telethon import events
from time import sleep
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r'\.meme'))
async def memehandler(event):
    client = event.client
    chat = await event.get_chat()
    await client.edit_message(event.message , "Getting You a meme")
    jsonD = requests.get('https://meme-api.herokuapp.com/gimme').json()
    try:
        await client.send_file(chat ,jsonD['url'] , caption=jsonD['title'] )
    except :
        print(jsonD['url'])
        await client.edit_message(event.message , "Sorry Unable to Process Request for meme")

    sleep(3)
    await event.message.delete()