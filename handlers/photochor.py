from telethon import  events
from telethon.tl.functions.photos import UploadProfilePhotoRequest


@events.register(events.NewMessage(outgoing=True, pattern=r'\.photuchor'))
async def handler(event):
    client = event.client
    if event.is_reply:
        replied = await event.get_reply_message()
        
        sender = replied.sender
        
        sender_profile_pic = await client.download_profile_photo(sender)
        await client(UploadProfilePhotoRequest(
            await client.upload_file(sender_profile_pic)
        ))
        await replied.reply("Phomtu chumra Liya. ab Kya krega \n \n Stole steals stolen your Photu ")