import logging
import os
from PIL import Image 
from telethon import TelegramClient , events

from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 1433221
api_hash = 'bf24ab6d9b49c3855f161f9d5aec707c'

client = TelegramClient('devil', api_id , api_hash)

# <---------------------- ping ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.ping'))
async def pingHandler(event):
    start = datetime.now()
    msg = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")

# <---------------------- pm hello ------------------->
@client.on(events.NewMessage(incoming=True , pattern='(?i)hello'))
async def greeting(event):
    chat = await event.get_chat()
    try:
        is_channel = chat.title
        pass
    except:
        
        await event.reply('hi!!! How are you?')
        
    
# <---------------------- Get Pfp ------------------->
@client.on(events.NewMessage(outgoing=True, pattern=r'\.photuchor'))
async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        
        sender = replied.sender
        
        sender_profile_pic = await client.download_profile_photo(sender)
        await client(UploadProfilePhotoRequest(
            await client.upload_file(sender_profile_pic)
        ))
        await replied.reply("Phomtu chumra Liya. ab Kya krega \n \n Stole steals stolen your Photu ")

# <---------------------- reverse text ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.ulta'))
async def reverseHandler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        replied_msg_rev = replied.message[::-1]
        await event.respond(replied_msg_rev)

# <---------------------- qutoly ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.quto'))
async def reverseHandler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        await replied.forward_to('@QuotLyBot')

# <---------------------- image to sticker   ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.itos'))
async def reverseHandler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        temp = await client.edit_message(event.message , "Processing ...")
        image = await replied.download_media()
        file = "devil.webp"
        if image.endswith((".webp", ".png", ".jpg")):
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

# <---------------------- sticker to image ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.stoi'))
async def reverseHandler(event):
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
    
        

# <---------------------- about me ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.me'))
async def reverseHandler(event):
    await client.edit_message(event.message , "Hey My name is Tony Stark \nBut somethime my friends call Me Shivam.\n\n**Want to know More About me?**\nGo [Here](https://devil-shiva.github.io/lucifer.github.io/)" , link_preview=False )


# <---------------------- alive ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.jinda'))
async def alivehandler(event):
    me = await client.get_me()
    username =  me.username
    phtou = await client.download_profile_photo(username)
    await client.edit_message(event.message  ,
        "Haan Jinda Hu bicy"
    )
    await event.respond(
        "My Master @{}\nWant to make Your Own Bot??"
        "\nBetter Watch Movies {}"
        
        .format(username , '@movie_united')
        ,file = phtou
        )
    await event.message.delete()
    os.remove(phtou)
    

client.start()
client.run_until_disconnected()