
from telethon import TelegramClient, client , events , utils

import requests

news_api = 'e97893d1464649e5813ff9b3f5b7e412'

@events.register(events.NewMessage(outgoing=True , pattern=r'\.news'))
async def newsHandler(event):
    chat = await event.get_chat()
    client = event.client
    try:
        country = event.message.raw_text.split()[1]
        await client.edit_message(event.message , "Getting News for {}".format(country))
        newsD = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api}').json()
        if newsD['totalResults'] == '0':
            await client.edit_message(event.message , "No News Found for entered Country Code\n\nAvailable Codes Are\n\n**ae\nar\nau\nbe\nbg\nbr\nca\nca\nch\ncn\nco\ncu\ncz\nde\neg\nfr\ngb\ngr\nhk\nhu\nid\nie\nil\nit\njp\nkr\nlt\nlv\nma\nmy\nng\nnl\nno\nnz\nph\npl\npt\nro\nrs\nru\nsa\nse\n\sg\nsi\nsk\nth\ntw\nua\nus\nve\nza**")
        else:   
            await client.edit_message(event.message , 
                "**[\n1. {}]({})**"
                "\n{}"
                "**[\n2. {}]({})**"
                "\n{}"
                "**[\n3. {}]({})**"
                "\n{}"
                "**[\n4. {}]({})**"
                "\n{}"
                .format(newsD['articles'][0]['title'], newsD['articles'][0]['url'], newsD['articles'][0]['description'] ,newsD['articles'][1]['title'], newsD['articles'][1]['url'], newsD['articles'][1]['description'] ,newsD['articles'][2]['title'], newsD['articles'][2]['url'], newsD['articles'][2]['description'] ,newsD['articles'][3]['title'], newsD['articles'][3]['url'], newsD['articles'][3]['description']) , link_preview=False)
        
    except:
        await client.edit_message(event.message , "No Country Entered. Getting Headlines of India")
        newsD = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}').json()
        
        await client.edit_message(event.message , 
        
        "**[\n1. {}]({})**"
        "\n{}"
        "**[\n2. {}]({})**"
        "\n{}"
        "**[\n3. {}]({})**"
        "\n{}"
        "**[\n4. {}]({})**"
        "\n{}"
        .format(newsD['articles'][0]['title'], newsD['articles'][0]['url'], newsD['articles'][0]['description'] ,newsD['articles'][1]['title'], newsD['articles'][1]['url'], newsD['articles'][1]['description'] ,newsD['articles'][2]['title'], newsD['articles'][2]['url'], newsD['articles'][2]['description'] ,newsD['articles'][3]['title'], newsD['articles'][3]['url'], newsD['articles'][3]['description']) , link_preview=False)
        
    