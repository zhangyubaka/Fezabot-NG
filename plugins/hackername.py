#!/usr/bin/env python3

async def hackerize(bot,msg):
	print("GET /hackize")
	name = msg['text'].split()[-1].lower()
	intable = 'aseigot'
	outtable = '4531607'
	table = str.maketrans(intable,outtable)
	try:
		await bot.sendChatAction(msg['chat']['id'], 'typing')
		await bot.sendMessage(msg['chat']['id'],name.translate(table))
	except:
		await bot.sendMessage(msg['chat']['id'],"Syntax: /hackize <String>")