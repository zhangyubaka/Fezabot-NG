from snownlp import SnowNLP

async def zici(bot,msg):
	text = msg['text'].split()
	text.pop(0)
	text = ''.join(text)
	sentiments = SnowNLP(text).sentiments
	threshold = 0.5 # If greater than 0.5, support it.
	if sentiments >= threshold:
		await bot.sendMessage(msg['chat']['id'],'好耶。',reply_to_message_id=msg['message_id'])
	elif sentiments < threshold:
		await bot.sendMessage(msg['chat']['id'],'不好耶。',reply_to_message_id=msg['message_id'])
	else:
		await bot.sendMessage(msg['chat']['id'],'喵喵喵？',reply_to_message_id=msg['message_id'])