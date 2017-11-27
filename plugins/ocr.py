#!/usr/bin/env python3

from tesserocr import PyTessBaseAPI
import io

async def ocr(bot,msg):
	print('GET /ocr')
	async with PyTessBaseAPI() as api:
		await bot.sendMessage(msg['chat']['id'],'Image Got!')
		api.SetImageFile(io.BytesIO(msg))
		api.Recognize()
		await bot.sendMessage(msg['chat']['id'],api.GetUTF8Text())
		await bot.sendMessage(msg['chat']['id'],api.AllWordsConfidence())