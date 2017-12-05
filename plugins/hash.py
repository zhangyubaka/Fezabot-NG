#!/usr/bin/env python3

import hashlib

async def hash(bot,msg):
	print('GET /hash')
	text = msg['text'].split()[-1]
	try:
		md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
		sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
		sha256 = hashlib.sha256(text.encode('utf-8')).hexdigest()
		sha512 = hashlib.sha512(text.encode('utf-8')).hexdigest()
		await bot.sendMessage(msg['chat']['id'],"md5"+' '+md5 +'\n'+'sha1'+' '+sha1+'\n'+'sha256'+' '+sha256+'\n'+'sha512'+' '+sha512)
	except:
		await bot.sendMessage(msg['chat']['id'],"Syntax: /hash <msg to be hash>")