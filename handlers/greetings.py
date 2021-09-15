
from telethon import  events


@events.register(events.NewMessage( func=lambda e: e.is_private,incoming=True , pattern='(?i)hello'))
async def greeting(event):
    await event.reply('hi!!! How are you?')