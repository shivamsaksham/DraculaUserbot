from handlers.approvepm import approvePm
from telethon import  events
from .approvepm import is_pm_verified
from telethon.tl import functions
import os

# is_pm_verified = approvepm.is_pm_verified

@events.register(events.NewMessage(incoming=True , func=lambda e: e.is_private))
async def pmPermit(event):
    client = event.client
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