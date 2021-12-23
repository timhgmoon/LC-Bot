import discord
from discord.ext import tasks, commands
import os
from datetime import datetime
from leetcode_data import GrabUrl
from dotenv import load_dotenv
import logging, time
load_dotenv()


# logging (recommended by discord documentation)
logging.basicConfig(level=logging.INFO)

# Grab token from .env and start discord bot
token = os.getenv('DISCORD_TOKEN')
# client = discord.Client()
client = commands.Bot(command_prefix='.')

now = datetime.now()
@client.event
async def on_ready():
    send_message.start()
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(hours=12)
async def send_message():
    channel = client.get_channel(922324853388890172)
    new_url = GrabUrl.getUrl()
    await channel.send(new_url)


@client.event
async def on_message(message):

    new_url = GrabUrl.getUrl()
    
    if message.author == client.user:
        return
    # testing 
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

    # will search stack over flow for questions/answer
    #not yet implemented
    if message.content.startswith('$solution'):
        await message.channel.send('asdf')

    # grabs random problem from leetcode
    if message.content.startswith('$random'):
        await message.channel.send(new_url)
    
    # if message.content.startswith('$start'):
        
    #     while(True):
    #         new_url = GrabUrl.getUrl()
    #         time.sleep(60)
    #         if(now.strftime("%H:%M") == "06:30"):
    #             await message.channel.send(new_url)
        
    

#run the discord bot(send in token)
client.run(token)

