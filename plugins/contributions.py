import aiohttp
import io
import cairosvg
#import aiofiles

global bot
async def getContribution(bot,msg):
    print('GET /Contributions')
    # Use 'chat' instead of 'from' to avoid sending to user instead of group.
    await bot.sendChatAction(msg['chat']['id'], 'upload_photo')
    # Get the SVG file
    async with aiohttp.ClientSession() as session:
    	async with session.get('https://github.com/users/' + msg['text'].split()[-1] + '/contributions') as resp:
    		await bot.sendPhoto(msg['chat']['id'],io.BytesIO(cairosvg.svg2png(await resp.read())) ,caption="GitHub Contributions for "+msg['text'].split()[-1])
    		#Convert to PNG file
    		#async with aiofiles.open('tmp.png', 'rb') as f:
    			