#!/usr/bin/env python3
from urllib.parse import unquote

async def urldecode(bot,msg):
	print('GET /urldecode')
	text = msg['text'].split()[-1]
	try:
		await bot.sendMessage(msg['chat']['id'],unquote(unquote(text)))
	except:
		await bot.sendMessage(msg['chat']['id'],"Request failed.")