import asyncio
from aiohttp import web
import telepot
import telepot.aio
from telepot.aio.loop import OrderedWebhook
from pprint import pprint
from plugins.contributions import getContribution
from plugins.help import botHelp
from config import TOKEN,PORT,URL

global bot


async def feeder(request):
    data = await request.text()
    webhook.feed(data)
    return web.Response(body='OK'.encode('utf-8'))

async def init(app, bot):
    app.router.add_route('GET', '/webhook', feeder)
    app.router.add_route('POST', '/webhook', feeder)

    await bot.setWebhook(URL)


async def handler(msg):
	pprint(type(msg))
	pprint(msg)
	try:
		if msg['text'].startswith('/contributions'):
			await getContribution(bot,msg)
		elif msg['text'].startswith('/start'):
			await bot.setMessage(msg['chat']['id'],'This is Feza Bot NG.')
		elif msg['text'].startswith('/zici'):
			pass
		elif msg['text'].startswith('/help'):
			await botHelp(bot,msg)
	except KeyError as e:
		pprint(e)


loop = asyncio.get_event_loop()

app = web.Application(loop=loop)
bot = telepot.aio.Bot(TOKEN, loop=loop)
webhook = OrderedWebhook(bot, {'chat': handler})

loop.run_until_complete(init(app, bot))

loop.create_task(webhook.run_forever())

web.run_app(app, port=PORT)