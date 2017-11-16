#!/usr/bin/env python3
import aiohttp

async def trueInteger(bot,msg):
	print('Get /trueRandom')
	await bot.sendChatAction(msg['chat']['id'], 'typing')
	mmax = msg['text'].split()[-1]
	mmin = msg['text'].split()[-2]
	mnum = msg['text'].split()[-3]
	try:
		async with aiohttp.ClientSession() as session:
			async with session.get('https://www.random.org/integers',params={'min':mmin,'max':mmax,'base':10,'col':1,'num':mnum,'rnd':'new','format':'plain'}) as resp:
				await bot.setMessage(msg['chat']['id'],resp.text)
	except:
		await bot.setMessage(msg['chat']['id'],"Request failed.")

