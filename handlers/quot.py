from telethon import events



@events.register(events.NewMessage(outgoing=True , pattern=r'\.quto'))
async def qutoHandler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        await replied.forward_to('@QuotLyBot')