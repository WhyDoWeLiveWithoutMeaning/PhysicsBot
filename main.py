import os

import discord
from discord.ext import commands

from HIDDEN import BOT_TOKEN

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

## BOT EVENTS
@client.event
async def on_ready():
    print("Online") 

## Load All Cogs
for file1 in os.listdir("."): # Loop through all files in the current directory
    print("1 " + file1)
    if os.path.isdir(os.path.join(os.path.abspath("."), file1)): # If the file is a directory
        for file2 in os.listdir(os.path.join(os.path.abspath("."), file1)):  
            print("2\t" + file2)
            if file2.endswith(".py"): # If the file is a .py file load it as a cog
                print("Loading: " + file2)
                client.load_extension(f"{file1}.{file2[:-3]}")
            elif os.path.isdir(os.path.join(os.path.join(os.path.abspath("."), file1), file2)): # If the file is a directory
                for file3 in os.listdir(os.path.join(os.path.join(os.path.abspath("."), file1), file2)): # Loop through all files in that directory
                    if file3.endswith(".py"): # If the file is a .py file load it as a cog
                        print("3\t\t" + file3)
                        print("Loading: " + file3)
                        client.load_extension(f"{file1}.{file2}.{file3[:-3]}")


client.run(BOT_TOKEN)