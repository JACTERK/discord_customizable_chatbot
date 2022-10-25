"""
Created on Sat Jul  9 11:58:34 2022

@author: Jacob Terkuc
"""

#Impliment gif sender
#Impiment chat context

import os, discord, functions, asyncio, random, settings, schedule

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from dotenv import load_dotenv

#grab tokens from .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

discord_client = discord.Client(intents=intents)

#console message to indicate the bot has come online.
@discord_client.event
async def on_ready():
    print(f'{discord_client.user} has connected to Discord! (use keyword [' + settings.trigger_name + "] to trigger)")

#message event
@discord_client.event
async def on_message(message):

    if message.author == discord_client.user:
        return
    


    #change 'summit' to what you want the bot to respond to in the server.
    if settings.trigger_name in message.content.lower():

        resp = functions.generate_response(message.content, settings.prompt)

        #Cleaning function
        print (resp)

        splitText = resp.split(": ")

        respC = splitText[len(splitText) - 1]

        if(len(resp) > 5):
            print("OpenAI API Pass")

            await asyncio.sleep(random.randrange(settings.time_to_wait_min, settings.time_to_wait_max)) #wait 1 to 3 seconds before passing

            async with message.channel.typing():
                await asyncio.sleep(functions.generate_typetime(resp))        #send the typing indicator for 3 to 6 seconds

            print("Pass to Discord API")                                      #status message send to console

            await message.channel.send(respC + ' ')                           #send resp (generated message) to discord
            return

        else:
            await message.channel.send(settings.default_response)


discord_client.run(DISCORD_TOKEN)

