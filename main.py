__author__ = "Feather Zhang"
import asyncio
from aiohttp import web
import telepot
import telepot.aio
from telepot.aio.loop import OrderedWebhook
import uvloop
from pprint import pprint
# Plugins
from plugins.contributions import getContribution
from plugins.help import botHelp
from config import TOKEN,PORT,URL
from plugins.trueRandom import trueInteger
from plugins.dns import getdns
from plugins.hackername import hackerize
from plugins.sadchildren import sad
from plugins.wttr import getWttr
from plugins.urldecode import urldecode
#from plugins.ocr import ocr
from plugins.translate import translate
from plugins.zici import zici
from plugins.kuaidi import kuaidi

async def feeder(request): # Copy/Pasting code from telepot examples
    data = await request.text()
    webhook.feed(data)
    return web.Response(body='OK'.encode('utf-8'))

async def init(app, bot): # Copy/Pasting code from telepot examples
    app.router.add_route('GET', '/webhook', feeder)
    app.router.add_route('POST', '/webhook', feeder)

    await bot.setWebhook(URL)


async def handler(msg):    # I may have to refactor this function, this is way too ugly. I just want a case-switch.
	pprint(telepot.flance(msg,long=True))	# Logging info...

	try: # Handle the commands
		if msg['text'].startswith('/contributions'):
			await getContribution(bot,msg)
		elif msg['text'].startswith('/start'):
			await bot.setMessage(msg['chat']['id'],'This is Feza Bot NG.')
		elif msg['text'].startswith('/help'):
			await botHelp(bot,msg)
		elif msg['text'].startswith('/random'):
			await trueInteger(bot,msg)
		elif msg['text'].startswith('/lookup'):
			await getdns(bot,msg)
		elif msg['text'].startswith('/hacker'):
			await hackerize(bot,msg)
		elif msg['text'].startswith('/sad'):
			await sad(bot,msg)
		elif msg['text'].startswith('/wttr'):
			await getWttr(bot,msg)
		elif msg['text'].startswith('/urldecode'):
			await urldecode(bot,msg)
		elif msg['text'].startswith('/ocr'): # Disable OCR due to poor effciency.
			#await ocr(bot,msg)
			pass
		elif msg['text'].startswith('/translate'):
			await translate(bot,msg)
		elif msg['text'].startswith('/support'):
			await zici(bot,msg)
		elif msg['text'].startswith('/kuaidi'):
			await kuaidi(bot,msg)
	except KeyError as e: # It may throw something at me. And I hate it.
		pprint(e)


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) # Using libuv for better performance
loop = asyncio.get_event_loop() # Get eventloop

app = web.Application(loop=loop)
bot = telepot.aio.Bot(TOKEN, loop=loop)
webhook = OrderedWebhook(bot, {'chat': handler}) # Create Webhook here.

loop.run_until_complete(init(app, bot))

loop.create_task(webhook.run_forever())

web.run_app(app, port=PORT)
