import discord 
import sysconfig
from discord import app_commands 
from discord.ext import commands 
import config
import os
import datetime
import random
from Atlas import randoming, pic_list, positive, gif_list
from h_gif import h_gif, w_gif
from m_aes import male
from f_aes import female
from c_aes import couple
import requests
import sqlite3
import re
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('TOKEN')

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



@client.tree.command(name = "help", description="shows the command list")
async def help(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " Command List ",
                          description= " </help:1135286623223959672> - shows the list of commands \n"+
                          " </info:1135286623223959673> - shows the list of available aesthetics \n"+
                          " </light:1135286623429468250> - shows the light academia related themes \n"+
                          " </dark:1135286623429468251> - shows the dark paradise related themes \n"+
                          " </pale:1135286623429468252>- shows the pale grunge related themes \n"+
                          " </fairy_core:1135286623429468253> - shows the fairycore related themes \n"+
                          " </sci_fi:1135286623429468254> - shows the sci-fi related themes \n" +
                          " </words:1135286623223959681> - shows unique and pleasant words\n"+
                          " </aesthetics:1135286623223959676> - shows random pictures for character and/or story inspiration \n"+
                          " </affirmations:1135286623223959679> - shows some positive vibes \n" +
                          " </aesthetic_gifs:1135286623223959675> - shows random gifs \n"+
                          "</male_aesthetics:1145051885783498824> - shows random male aesthetics \n"+
                          "</female_aesthetics:1145051885783498825> - shows random female aesthetics \n"+
                          "</couple_aesthetics:1145051885783498826> - shows random couple aesthetics \n"+
                          " </hug:1145051885783498822> - gives a warm hug to whoever you want \n"+
                          "</wave:1145051885783498823> - wave at anyone you want\n",
                        
                          color=discord.Color.dark_orange())
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1104408296967897170/fall-autumn.gif")
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used help."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message( embed = embed, ephemeral=False)

@client.tree.command(name = "hello", description="prints hello")
async def hello(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    
    data = {"content": f"User{user_name}({user_id}) used the /hello command."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message("Hello", ephemeral=False)

@client.tree.command(name = "hug", description="send a warm hug")  

async def hug(interaction: discord.Interaction, member:discord.Member):
    user_ = interaction.user
    member1 = member
    
    embed = discord.Embed(title=f"{user_} sends a hug at {member1}'s way", color=discord.Color.dark_red())
    hugs = random.choice(h_gif)
    embed.set_image(url=hugs)
    embed.set_footer(text="Have a nice day!")  
    await interaction.response.send_message(embed=embed)


@client.tree.command(name = "wave", description="wave")  

async def wave(interaction: discord.Interaction, member:discord.Member):
    user_ = interaction.user
    member1 = member    
    embed = discord.Embed(title=f"{user_} is waving at {member1}", color=discord.Color.dark_red())
    waves = random.choice(w_gif)
    embed.set_image(url=waves)
    embed.set_footer(text="Have a nice day!")  
    await interaction.response.send_message(embed=embed)
    
@client.tree.command(name= "male_aesthetics", description="Shows different male aesthetic character/story inspiration")
async def male_aesthetics(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    male_= random.choice(male) 
    embed.set_image(url=male_)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used aesthetics."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)  
    
@client.tree.command(name= "female_aesthetics", description="Shows different female aesthetic character/story inspiration")
async def female_aesthetics(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    female_= random.choice(female) 
    embed.set_image(url=female_)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used aesthetics."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)   
    
@client.tree.command(name= "couple_aesthetics", description="Shows different couple aesthetic character/story inspiration")
async def couple_aesthetics(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    couple_= random.choice(couple) 
    embed.set_image(url=couple_)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used aesthetics."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False) 
    
     
@client.tree.command(name = "info", description="provides information about different aesthetics provided by the bot")
async def info(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= "Aesthetics ",
        description="  aes·thet·ic \n" + " noun \n" + " - a branch of philosophy dealing with the nature of beauty, art, and taste and with the creation and appreciation of beauty \n" +
                   "  - a particular theory or conception of beauty or art : a particular taste for or approach to what is pleasing to the senses and especially sight \n" +
                   "  - a pleasing appearance or effect : beauty",
        color= discord.Color.dark_teal())
    
    embed.set_author(name= " Aesthetic Information ", 
                     icon_url="https://cdn.discordapp.com/attachments/1099693772608122982/1102263222121283704/images_3.jpeg")
  
    embed.add_field(name= "Dark Paradise Aesthetics ",
                    value = " The Dark Paradise aesthetic focuses on images of serenity with a veil of darkness laid over it to rouse a sense of dark calmness. Dark Paradise revolves around visually dark photos, as if taken in the dark or in the late evening")
    
    embed.add_field(name=" Light Academia Aesthetic",
                    value="Light academia aesthetic is often associated with classic studies and is characterised by its focus on soft and muted colours, vintage clothing, and a romanticised view of the world")
    
    embed.add_field(name=" Pale Aesthetic",
                    value= " Pale Grunge or Pale Aesthetic is an aesthetic based on simple photos with a color palette based on white, grey, black, green, and blue.")
    
    embed.add_field(name= "Fairycore Aesthetic",
                    value=" Fairycore, also known as Fairy Folk, is a fantasy themed aesthetic that centres predominantly around fairy (alternatively spelled faerie) and elf mythology. Visuals include nature, soft pastels, butterflies, magic, flowers, soft animals like bunnies, and the vibe of springtime.")
    
    embed.add_field(name=" Sci-Fi Aesthetic",
                    value = "The Used Future aesthetic is a hallmark of the 70s and 80s sci-fi era. It imagines a future in which some things have evolved well beyond modern imagination, while others remain almost identical to their contemporary form. Alien features one of the best possible examples.")
    
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1105891973883244595/TightWhoppingCreature-size_restricted.gif")
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used info."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message( embed = embed, ephemeral=False)    


@client.tree.command(name= "aesthetic_gifs", description="Shows different aesthetic gifs for character/story inspiration")
async def aesthetic_gifs(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    rand_gif= random.choice(gif_list) 
    embed.set_image(url=rand_gif)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used aesthetics."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)    
    

@client.tree.command(name= "aesthetics", description="Shows one different aesthetic pictures from pinterest for character/story inspiration")
async def aesthetics(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    rand_ = random.choice(randoming) 
    embed.set_image(url=rand_)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used aesthetics."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)    
    
    
    
    
@client.tree.command(name= "affirmations", description="Shows one liners/affirmations")
async def affirmations(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.light_gray())
    pic = random.choice(positive) 
    embed.set_image(url=pic)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used affirmations."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)
    
    
    

@client.tree.command(name= "words", description="Shows unique words")
async def words(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(title= " ",
                          description= "The pictures belong to their respective owners",
                          color=discord.Color.dark_teal())
    pic = random.choice(pic_list) 
    embed.set_image(url=pic)
    embed.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used words."}
    
    response = requests.post(webhook_url, json=data)
    await interaction.response.send_message(embed=embed, ephemeral=False)
    
    
    
@client.tree.command(name = "light", description="shows the light academia themed aesthetics")  
@app_commands.describe(choose_theme = " Mention the number of the theme you want to see")
async def light(interaction: discord.Interaction, choose_theme: int):  
    user_id = interaction.user.id
    user_name = interaction.user.name 
    embed = discord.Embed(
        title='Light Academia Related themes',
        description=' ',
        color = discord.Color.lighter_grey(),
        url="https://in.pinterest.com/search/pins/?rs=ac&len=2&q=light%20academia%20aesthetic&eq=light%20academia&etslf=6080")
    
    embed.set_author(name = " Light Aesthetics by SardonicBeauty")
    embed.add_field(name = "Theme 1", value = " ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102635734164324372/l1.png")
    embed.set_footer(text="Have a nice day!")
    
    embed1 = discord.Embed(
        title='Light Academia Related themes',
        color = discord.Color.light_grey(),
        url="https://in.pinterest.com/search/pins/?rs=ac&len=2&q=light%20academia%20aesthetic&eq=light%20academia&etslf=6080")
    
    embed1.set_author(name = " Light Aesthetics by SardonicBeauty")
    embed1.add_field(name = "Theme 2", value = " ")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102635734818619522/l2.png")
    embed1.set_footer(text="Have a nice day!")
    
 
    embed2 = discord.Embed(
        title='Light Academia Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url="https://in.pinterest.com/search/pins/?q=light%20aesthetic&rs=typed")
    
    embed2.set_author(name = " Light Aesthetics by SardonicBeauty")
    embed2.add_field(name = "Theme 3", value = " ")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102631842609377310/l3.png")
    embed2.set_footer(text="Have a nice day!")
    
    
    embed3 = discord.Embed(
        title='Light Academia Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url="https://in.pinterest.com/search/pins/?q=light%20aesthetic&rs=typed")
    
    embed3.set_author(name = " Light Aesthetics by SardonicBeauty")
    embed3.add_field(name = "Theme 4", value = " ")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102631843179798578/l4.png")
    embed3.set_footer(text="Have a nice day!")
    data = {"content": f"User {user_name}({user_id}) used light."}
    
    response = requests.post(webhook_url, json=data)
    if choose_theme==1:
         await interaction.response.send_message(embed = embed, ephemeral=False)
         
    elif choose_theme==2:
        await interaction.response.send_message(embed = embed1, ephemeral=False)
        
    elif choose_theme==3:
        await interaction.response.send_message(embed = embed2, ephemeral=False)
        
    else:
        await interaction.response.send_message(embed = embed3, ephemeral=False)     
        
        
@client.tree.command(name = "dark", description="shows the dark paradise themed aesthetics ")  
@app_commands.describe(choose_theme = " Mention the number of the theme you want to see")
async def dark(interaction: discord.Interaction, choose_theme: int):  
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(
        title='Dark Paradise Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url= "https://in.pinterest.com/search/pins/?q=dark&rs=rs&eq=&etslf=1113")
    embed.set_author(name = " Dark Aesthetics by SardonicBeauty")
    embed.add_field(name = "Theme 1", value = " ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1101926119327944744/d1.png")
    embed.set_footer(text="Have a nice day!")
    
    embed1 = discord.Embed(title='Dark Paradise Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url= "https://in.pinterest.com/search/pins/?q=dark&rs=rs&eq=&etslf=1113")
    embed1.set_author(name = " Dark Aesthetics by SardonicBeauty ")
    embed1.add_field(name = "Theme 2", value = " ") 
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102119479388934245/d2.png")
    embed1.set_footer(text="Have a nice day!")   
    
    embed2 = discord.Embed(title='Dark Paradise Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url= "https://in.pinterest.com/search/pins/?q=dark&rs=rs&eq=&etslf=1113")
    embed2.set_author(name = " Dark Aesthetics by SardonicBeauty ")
    embed2.add_field(name = "Theme 3", value = " ") 
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102203063177052200/d3.png")
    embed2.set_footer(text="Have a nice day!")  
    
    embed3 = discord.Embed(title='Dark Paradise Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url= "https://in.pinterest.com/search/pins/?q=dark&rs=rs&eq=&etslf=1113")
    embed3.set_author(name= "  Dark Aesthetics by SardonicBeauty ")
    embed3.add_field(name = "Theme 4", value = " ") 
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102203062778605688/d4.png") 
    embed3.set_footer(text="Have a nice day!") 
    data = {"content": f"User {user_name}({user_id}) used dark."}
    
    response = requests.post(webhook_url, json=data)
    
    if choose_theme==1:
         await interaction.response.send_message(embed = embed, ephemeral=False)
         
    elif choose_theme==2:
        await interaction.response.send_message(embed = embed1, ephemeral=False)
        
    elif choose_theme==3:
        await interaction.response.send_message(embed = embed2, ephemeral=False)
        
    else:
        await interaction.response.send_message(embed = embed3, ephemeral=False)  
        
        
@client.tree.command(name = "pale", description="shows the pale grunge themed aesthetics")  
@app_commands.describe(choose_theme = " Mention the number of the theme you want to see")
async def pale(interaction: discord.Interaction, choose_theme: int): 
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(
        title='Pale Grunge Related themes',
        description=' ',
        color = discord.Color.dark_gray(),
        url="https://in.pinterest.com/search/pins/?q=pale%20grunge%20aesthetic&rs=typed")
    
    embed.set_author(name = " Pale Aesthetics by SardonicBeauty")
    embed.add_field(name = "Theme 1", value = " ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103359374388379708/p1.png")
    embed.set_footer(text="Have a nice day!")
   
    
    embed1 = discord.Embed(
        title='Pale Grunge Related themes',
        description=' ',
        color = discord.Color.light_grey(),
        url="https://in.pinterest.com/search/pins/?q=pale%20white%20aesthetic%20grunge&rs=typed")
    
    embed1.set_author(name = " Pale Aesthetics by SardonicBeauty")
    embed1.add_field(name = "Theme 2", value = " ")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103359373679538246/p2.png")
    embed1.set_footer(text="Have a nice day!")
    
 
    embed2 = discord.Embed(
        title='Pale Grunge Related themes',
        description=' ',
        color = discord.Color.blue(),
        url="https://in.pinterest.com/search/pins/?q=pale%20blue%20aesthetic%20grunge&rs=guide&add_refine=pale%20blue%20aesthetic%20grunge%7Cguide%7Cword%7C4")
    
    embed2.set_author(name = " Pale Aesthetics by SardonicBeauty")
    embed2.add_field(name = "Theme 3", value = " ")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103359373109117000/p3.png")
    embed2.set_footer(text="Have a nice day!")
    
    
    embed3 = discord.Embed(
        title='Pale Grunge Related themes',
        description=' ',
        color = discord.Color.dark_green(),
        url="https://in.pinterest.com/search/pins/?q=pale%20green%20aesthetic%20grunge&rs=typed")
    
    embed3.set_author(name = " Pale Aesthetics by SardonicBeauty")
    embed3.add_field(name = "Theme 4", value = " ")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103359372563853452/p4.png")
    embed3.set_footer(text="Have a nice day!")
    
    data = {"content": f"User {user_name}({user_id}) used pale."}
    
    response = requests.post(webhook_url, json=data)
    if choose_theme==1:
         await interaction.response.send_message(embed = embed, ephemeral=False)
         
    elif choose_theme==2:
        await interaction.response.send_message(embed = embed1, ephemeral=False)
        
    elif choose_theme==3:
        await interaction.response.send_message(embed = embed2, ephemeral=False)
        
    else:
        await interaction.response.send_message(embed = embed3, ephemeral=False) 
        
        
@client.tree.command(name = "fairy_core", description="shows the fairycore related themed aesthetics")  
@app_commands.describe(choose_theme = " Mention the number of the theme you want to see")
async def fairy_core(interaction: discord.Interaction, choose_theme: int): 
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(
        title='Fairycore related themes',
        description=' ',
        color = discord.Color.dark_teal(),
        url="https://in.pinterest.com/search/pins/?rs=ac&len=2&q=fairy%20aesthetic&eq=fairy&etslf=4033")
    
    embed.set_author(name = " Fairycore Aesthetics by SardonicBeauty")
    embed.add_field(name = "Theme 1", value = " ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102576926067015763/f1.png")
    embed.set_footer(text="Have a nice day!")
   
    
    embed1 = discord.Embed(
        title='Fairycore related themes',
        description=' ',
        color = discord.Color.teal(),
        url="https://in.pinterest.com/search/pins/?rs=ac&len=2&q=fairy%20aesthetic&eq=fairy&etslf=4033")
    
    embed1.set_author(name = " Fairycore Aesthetics by SardonicBeauty")
    embed1.add_field(name = "Theme 2", value = " ")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102577891474157709/f2.png")
    embed1.set_footer(text="Have a nice day!")
    
 
    embed2 = discord.Embed(
        title='Fairycore related themes',
        description=' ',
        color = discord.Color.teal(),
        url="https://in.pinterest.com/search/pins/?rs=related_searches_organic&q=woodland%20fairy%20aesthetic&source_id=0003e55656eb3898rs")
    
    embed2.set_author(name = " Fairycore Aesthetics by SardonicBeauty")
    embed2.add_field(name = "Theme 3", value = " ")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102620294058868837/f3.png")
    embed2.set_footer(text="Have a nice day!")
    
    
    embed3 = discord.Embed(
        title='Fairycore related themes',
        description=' ',
        color = discord.Color.dark_teal(),
        url="https://in.pinterest.com/search/pins/?rs=ac&len=2&q=fairy%20aesthetic&eq=fairy&etslf=4033")
    
    embed3.set_author(name = " Fairycore Aesthetics by SardonicBeauty")
    embed3.add_field(name = "Theme 4", value = " ")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1102620293563957258/f4.png")
    embed3.set_footer(text="Have a nice day!")
    
    data = {"content": f"User {user_name}({user_id}) used fairy_core."}
    
    response = requests.post(webhook_url, json=data)
    if choose_theme==1:
         await interaction.response.send_message(embed = embed, ephemeral=False)
         
    elif choose_theme==2:
        await interaction.response.send_message(embed = embed1, ephemeral=False)
        
    elif choose_theme==3:
        await interaction.response.send_message(embed = embed2, ephemeral=False)
        
    else:
        await interaction.response.send_message(embed = embed3, ephemeral=False)
        
        
@client.tree.command(name = "sci_fi", description="shows the sci-fi related themed aesthetics")  
@app_commands.describe(choose_theme = " Mention the number of the theme you want to see")
async def sci_fi(interaction: discord.Interaction, choose_theme: int):
    user_id = interaction.user.id
    user_name = interaction.user.name
    embed = discord.Embed(
        title='Sci-Fi related themes',
        description=' ',
        color = discord.Color.dark_grey())
    embed.set_author(name = " Sci-Fi Aesthetics by SardonicBeauty")
    embed.add_field(name = "Theme 1", value = " ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103940359786078289/s1.png")
    embed.set_footer(text="Have a nice day!")
    
    
    embed1 = discord.Embed(
    title='Sci-Fi related themes',
    description=' ',
    color = discord.Color.dark_blue(),
    url = "https://in.pinterest.com/search/pins/?q=sci%20fi%20aesthetic&rs=rs&eq=&etslf=3381")
    embed1.set_author(name = " Sci-Fi Aesthetics by SardonicBeauty")
    embed1.add_field(name = "Theme 2", value = " ")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103940360884990023/s2_1.png")
    embed1.set_footer(text="Have a nice day!")
    
    
    embed2 = discord.Embed(
    title='Sci-Fi related themes',
    description=' ',
    color = discord.Color.dark_purple(),
    url = "https://in.pinterest.com/search/pins/?q=sci%20fi%20aesthetic&rs=rs&eq=&etslf=3381")
    embed2.set_author(name = " Sci-Fi Aesthetics by SardonicBeauty")
    embed2.add_field(name = "Theme 3", value = " ")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103940360360693780/s3.png")
    embed2.set_footer(text="Have a nice day!")
    
    
    embed3 = discord.Embed(
    title='Sci-Fi related themes',
    description=' ',
    color = discord.Color.red(),
    url = "https://in.pinterest.com/search/pins/?q=science%20fiction%20aesthetic&rs=rs&eq=&etslf=1231")
    embed3.set_author(name = " Sci-Fi Aesthetics by SardonicBeauty")
    embed3.add_field(name = "Theme 4", value = " ")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1099693772608122982/1103940826914099200/s4.png")
    embed3.set_footer(text="Have a nice day!")
    
    data = {"content": f"User {user_name}({user_id}) used sci_fi."}
    
    response = requests.post(webhook_url, json=data)
    if choose_theme==1:
         await interaction.response.send_message(embed = embed, ephemeral=False)
         
    elif choose_theme==2:
        await interaction.response.send_message(embed = embed1, ephemeral=False)
        
    elif choose_theme==3:
        await interaction.response.send_message(embed = embed2, ephemeral=False)
        
    else:
        await interaction.response.send_message(embed = embed3, ephemeral=False)
        
client.run(bot_token)
