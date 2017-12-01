from vocabulary.vocabulary import Vocabulary as vb

async def translate(bot,msg):
	try:
		print('GET /translate')
		with msg['text'].split() as text:
			source = text[1]
			dest = text[2]
			word = text[3]
			await bot.sendMessage(msg['chat']['id'],vb.translate(word,source_lang=source,dest_lang=dest))
	except:
		await bot.sendMessage(msg['chat']['id'],"Syntax: /translate sourceLang destLang words. Eg: /translate en zh car"
