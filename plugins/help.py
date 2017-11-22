async def botHelp(bot,msg):
	print('GET /Help')
	await bot.sendChatAction(msg['chat']['id'], 'typing')
	await bot.sendMessage(msg['chat']['id'],
		"""
		This is Fezabot-NG.
		The owner is porting all feature currently.

		Features that are available now:

		/contributions username : Get @username's contributions chat on GitHub.

		""")