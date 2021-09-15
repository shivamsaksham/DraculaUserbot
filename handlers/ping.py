from telethon import  events
from datetime import datetime



@events.register(events.NewMessage(outgoing=True , pattern=r'\.ping'))
async def pingHandler(event):
    start = datetime.now()
    msg = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")