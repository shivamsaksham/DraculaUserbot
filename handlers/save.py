from telethon import  events
from time import sleep




@events.register(events.NewMessage(outgoing=True , pattern=r'\.save'))
async def saveHandler(event):
    client = event.client
    if event.is_reply:
        replied = await event.get_reply_message()
        is_tag = event.message.raw_text.split()
        try:
            tag = is_tag[1]
            await client.send_message('me' , "#{}".format(tag))
        except:
            await client.edit_message(event.message , "No Tag..")
            sleep(1)
        me = await client.get_me()
        await client.forward_messages('me' , replied)
        await client.edit_message(event.message , "Saved To your Cloud [Here](https://t.me/{})".format(me.username) , link_preview=False)
        sleep(3)
        await event.message.delete()