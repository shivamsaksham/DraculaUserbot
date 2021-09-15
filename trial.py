import logging
import os
from time import sleep
from PIL import Image 
from telethon import TelegramClient , events , utils
from telethon.tl import functions

from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime

from telethon.tl.types import PeerUser, User



logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 1433221
api_hash = 'bf24ab6d9b49c3855f161f9d5aec707c'

client = TelegramClient('devil', api_id , api_hash)

is_pm_verified = []
is_pm_disapproved= []

@client.on(events.NewMessage(outgoing=True , pattern=r'\.ap' ))
async def approvePm(event):
    chat = await event.get_chat()
    is_pm_verified.append(chat.id)
    await client.edit_message(event.message , "User Verified..")
    sleep(2)
    await event.message.delete()

# <---------------------- approve ------------------->
@client.on(events.NewMessage(incoming=True , func=lambda e: e.is_private))
async def pmPermit(event):
    chat = await event.get_chat()
    msg_krne_wala = chat.username
    me = await client.get_me()
    if (chat.id in is_pm_verified):
        return
    else:
        photu = await client.download_profile_photo(me.username)
        await client.send_message(chat , "Hey!! I am Gabbar UserBot of My Master [Dracula](@{})\n\nMy Master is a Very busy Person. If you are here for timepass then please FO. \n\nIf want some Help, Join [Here](https://t.me/team_HackTwist). My master will try to see your PM whenever he gets Time.\n\nThank You!!".format(me.username) , file=photu , link_preview=False)
        await client(functions.contacts.BlockRequest(id=msg_krne_wala))
        os.remove(photu)
        
# <---------------------- ping ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.ping'))
async def pingHandler(event):
    start = datetime.now()
    msg = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")

# <---------------------- pm hello ------------------->
@client.on(events.NewMessage( func=lambda e: e.is_private,incoming=True , pattern='(?i)hello'))
async def greeting(event):
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

# <---------------------- Save to saved msg ------------------->
@client.on(events.NewMessage(outgoing=True , pattern=r'\.save'))
async def saveHandler(event):
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