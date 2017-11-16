#!/usr/bin/env python3

import aiodns

async def getdns(bot,msg):
	async with aiodns.DNSResolver() as r:
		re = await r.query(msg['text'].split()[-2],msg['text'].split()[-1])
		await bot.sendMessage(msg['chat']['id'],re)