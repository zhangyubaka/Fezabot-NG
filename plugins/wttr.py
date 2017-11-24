#!/usr/bin/env python3
import aiohttp
import io


async def getWttr(bot,msg):
	print('GET /wttr')
	url = "http://wttr.in/"+msg['text'].split()[-1]+".png"
	async with aiohttp.ClientSession as session:
		async with session.get(url=url) as resp:
			await bot.sendPhoto(msg['chat']['id'],io.BytesIO(await resp.read()))
