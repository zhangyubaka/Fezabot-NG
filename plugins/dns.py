#!/usr/bin/env python3

import aiodns

async def getdns(bot,msg):
	print('GET /dns')
	try:
		async with aiodns.DNSResolver() as r:
			re = await r.query(msg['text'].split()[-2],msg['text'].split()[-1])
			await bot.sendMessage(msg['chat']['id'],re)
	except:
		await bot.sendMessage(msg['chat']['id'],"Syntax: /lookup <Hostname> <Type> ")