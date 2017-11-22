#!/usr/bin/env python3
import aiofiles
import os
import random

DIR = '/root/sadchildren/'

async def sad(bot,msg):
	print('GET /sad')
	file = random.choice(os.listdir(DIR))
	async with aiofiles.open(file) as f:
		await bot.sendPhoto(msg['chat']['id'],f ,caption=f.name)