from telethon import events
import os
from PIL import Image 

@events.register(events.NewMessage(outgoing=True , pattern=r'\.stoi'))
async def stoiHandler(event):
    client = event.client
    if event.is_reply:
        replied = await event.get_reply_message()
        temp = await client.edit_message(event.message , "Processing ...")
        image = await replied.download_media()
        file = "devil.png"
        if image.endswith((".webp", ".png")):
            c = Image.open(image)
            c.save(file)
        else:
            await client.edit_message(event.message , "Reply to any Image")
        await event.reply(file=file)
        await temp.delete()
        os.remove(file)
        os.remove(image)
    else:
        await client.edit_message(event.message , "Reply to any Image")