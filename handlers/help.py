from telethon import  events


@events.register(events.NewMessage(outgoing=True , pattern=r'\.help'))
async def helpHandler(event):
    client = event.client
    await client.edit_message(event.message , "Available Commands For Gabbar Userbot\n\n`.ap` - Approve pm\n`.ping` - pong\n`.photuchor` - reply to someone to get his profile pic as yours\n`.save` - save that message to SavedMessage\n`.ulta` - reply a text to reverse it\n`.quto` - reply to text to make It sticker\n`.itos` - Change Image to sticker\n`.stoi` - change sticker to image\n`.iam` - a intro dialogue\n`.jinda` - Check that your bot is alive\`.meme` - Get a Random Meme")