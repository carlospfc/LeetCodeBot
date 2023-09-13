import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import scraper

load_dotenv()

# Discord token
TOKEN = os.getenv('TOKEN')

# This gives the bot all the permissions in the server
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
# Shows in terminal that the bot has connected to the Discord server
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # Checks if the author of the message was bot itself
    if message.author == client.user:
        return
    if "!leet" == message.content.lower():
        await message.channel.send('Hello, I am LeetBot! Please select a problem difficulty. Type !leeteasy , !leetmedium , or !leethard.')
    # Checks if command is being sent; makes user input all lowercase to compare string values
    elif "!leeteasy" == message.content.lower():
        await message.channel.send(scraper.random_easy())
    elif "!leetmedium" == message.content.lower():
        await message.channel.send(scraper.random_medium())
    elif "!leethard" == message.content.lower():
        await message.channel.send(scraper.random_hard())


# Embed format
# embedVar = discord.Embed(title="", description="Desc", color=0xFF7F24)
# embedVar.add_field(name="Field1", value="hi", inline=False)
# await message.channel.send(embed=embedVar)    

client.run(TOKEN)
 