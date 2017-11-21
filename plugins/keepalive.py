#!/usr/bin/env python3

#import 
from peony import PeonyClient
import datetime
from dateutil.parser import parse
from trusted import userid

creds = dict(consumer_key=YOUR_CONSUMER_KEY,
             consumer_secret=YOUR_CONSUMER_SECRET,
             access_token=YOUR_ACCESS_TOKEN,
             access_token_secret=YOUR_ACCESS_TOKEN_SECRET) #Init a async client

client = PeonyClient(**creds)



async def isAlive(bot):

	latest = await client.api.statuses.user_timeline.get(screen_name="screenname")
	now = datetime.datetime.now(datetime.timezone.utc)
	time = datetime.datetime.now(datetime.timezone.utc) - parse(latest.created_at)
	if time.days > 2:
		await bot.sendMessage(bot.sendMessage(msg['chat']['id'],"""
			The Twitter account of `PlaceHolder` has been nonactive for over 2 days, now sending life confirmation request to pre-defined trusted user, please confirm this user life activitiy.
			You may send confirmation email to confirm@oao.moe with email titiled 'Confirmed' (Case Sensitive)
			""")

