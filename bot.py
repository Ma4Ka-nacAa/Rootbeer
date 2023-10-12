# Imports
import discord,datetime,os,conf
intents = discord.Intents.all()
from discord.ext import tasks

# Main bot function
def run_discord_bot():
    client = discord.Client(intents=intents)
    TOKEN = conf.TOKEN
    channelId = conf.channel_id
    channel = conf.channel
    content = conf.content
    roleId = conf.roleId

    # Rootbeer number
    if os.path.exists('num.txt') == False:
        with open('num.txt','w') as f:
            f.write('0')
            f.close()
            messageNumber = 0
    else:
        with open('num.txt','r') as f:
            messageNumber = sum([int(x) for x in f.read().split()])
            f.close()

    # Bot start
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        rootbeer.start()
    
    # Rootbeer loop
    @tasks.loop(minutes={conf.timeAmount})
    async def rootbeer():
        # The stupid thing that took me like idk forever to make but it works ig idk at this point
        with open('num.txt','r') as f:
            messageNumber = sum([int(x) for x in f.read().split()])
            f.close()
        with open('num.txt','w') as f:
            messageNumber += 1
            f.write(str(messageNumber))
            f.close()
        
        # Channel id
        channel = client.get_channel(channelId)
        
        # Message Number
        if messageNumber % conf.pingNum == 0:
            await channel.send(f'<@&{roleId}> Rootbeer #{messageNumber}!')
        else:
            await channel.send(f'#{messageNumber}')

        # Sending the message
        await channel.send(content)
        print(f'Posted \'{content}\' into #{channel} at {datetime.datetime.now()}')

    client.run(TOKEN)