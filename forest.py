import discord
import sysconfig
from discord import app_commands 
from discord.ext import commands 
import config
import os
import datetime
import random
import requests


intents = discord.Intents.default() 
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents = intents)
webhook_url = 'https://discord.com/api/webhooks/1118140114514755684/ijYto78EQ8pQetqBoivurndUoVUw9tygqd7jeGtKBydAR3RKB8a5siz5YBAgeTgOn95w'


    
@client.event
async def on_ready():
    print("The Bot is ready")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        
        
@client.tree.command(name = "hello", description="prints hello")
async def hello(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    
    data = {"content": f"User{user_name}({user_id}) used the /hello command."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message("Hello", ephemeral=False) 
    
client.run('MTEwMTkyNzI4MTA5MTQzMjQ0OA.Gt3Pwp.q95CyRP7p5dmyxYIWtdBtcrNmnbyNK2AzJ3EmE')