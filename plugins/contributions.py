import aiohttp
import cairosvg
import aiofiles

global bot
async def getContribution(bot,msg):
    print('Get /Contributions')
    # Use 'chat' instead of 'from' to avoid sending to user instead of group.
    await bot.sendChatAction(msg['chat']['id'], 'upload_photo')
    # Get the SVG file
    async with aiohttp.ClientSession() as session:
    	async with session.get('https://github.com/users/' + msg['text'].split()[-1] + '/contributions') as resp:
    		cairosvg.svg2png(await resp.read(),write_to='tmp.png')
    		async with aiofiles.open('tmp.png', 'rb') as f:
    			await bot.sendPhoto(msg['chat']['id'],f ,caption="GitHub Contributions for "+msg['text'].split()[-1])#reply_to_message_id=msg['message_id']
    #r = requests.get('https://github.com/users/' + msg['text'].split()[-1] + '/contributions',stream=True)
    # Convert into PNG file.
    #cairosvg.svg2png(r.raw.data,write_to='tmp.png')
    