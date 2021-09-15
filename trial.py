
import logging
from telethon import TelegramClient
import handlers.news , handlers.alive , handlers.stoi , handlers.itos , handlers.iam , handlers.quot , handlers.reverse , handlers.save , handlers.photochor , handlers.greetings , handlers.ping , handlers.pmpermit , handlers.approvepm , handlers.meme , handlers.help




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 1433221
api_hash = 'bf24ab6d9b49c3855f161f9d5aec707c'

client = TelegramClient('devil', api_id , api_hash)






# <---------------------- help ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.help.helpHandler)

# <---------------------- news ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.news.newsHandler)


# <---------------------- meme ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.meme.memehandler)

# <---------------------- approve pm ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.approvepm.approvePm)

# <---------------------- pmpermit ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.pmpermit.pmPermit)
        
# <---------------------- ping ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.ping.pingHandler)

# <---------------------- pm hello ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.greetings.greeting)
        
    
# <---------------------- Get Pfp ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.photochor.handler)

# <---------------------- Save to saved msg ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.save.saveHandler)

# <---------------------- reverse text ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.reverse.reverseHandler)

# <---------------------- qutoly ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.quot.qutoHandler)

# <---------------------- image to sticker   ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.itos.itosHandler)

# <---------------------- sticker to image ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.stoi.stoiHandler)

# <---------------------- about me ------------------->
with client as dracula:
    dracula.add_event_handler(handlers.iam.iamHandler)

# <---------------------- alive ------------------->

with client as dracula:
    dracula.add_event_handler(handlers.alive.alivehandler)

    

client.start()
client.run_until_disconnected()