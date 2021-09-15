from telethon import  events

from time import sleep

is_pm_verified = []

@events.register(events.NewMessage(outgoing=True , pattern=r'\.ap' ))
async def approvePm(event):
    client = event.client
    chat = await event.get_chat()
    if chat.id in is_pm_verified:
        await client.edit_message(event.message , "User Already Verified..")
    else:
        is_pm_verified.append(chat.id)
        await client.edit_message(event.message , "User Verified..")
    sleep(2)
    await event.message.delete()