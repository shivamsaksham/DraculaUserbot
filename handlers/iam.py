from telethon import  events


@events.register(events.NewMessage(outgoing=True , pattern=r'\.iam'))
async def iamHandler(event):
    client = event.client
    me = await client.get_me()
    await client.edit_message(event.message , "Hey My name is Tony Stark \nBut sometime my friends call Me {}.\n\n**Want to know More About me?**\nGo [Here](https://devil-shiva.github.io/lucifer.github.io/)".format(me.username) , link_preview=False )
