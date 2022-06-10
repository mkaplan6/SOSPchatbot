from msilib.schema import File
from discord.ext import commands
from discord import Embed
import discord
import os
import random

# Sources (for me)
# Discord dev page: https://discord.com/developers/applications/983182266480078848/bot
# Original file on replit: https://replit.com/@mkaplan6/SOSP22chatBot#main.py

# This is the code for Botlionis3, a discord chatbot for the discord server of my friend group.
# A lot of it is inside jokes and things that don't mean much to most people, but it was fun
# and educational creating this and it is my first ever python project. 

client = commands.Bot(command_prefix = '!')

# notifies the channel when the bot begins running
@client.event
async def on_ready():
    general_channel = client.get_channel(890621877192654870)
    await general_channel.send("I am awake. View my commands with !functions")


client.responsesToNames = ["I love that guy", "I hate that guy", "That guy smells", "What a weirdo",
                        "Not a fan", "Big fan of that guy", "I shall slay him", "He shall fall to my blade",
                        "he shant survive the winter"]
# hi hungry im dad, anti-milwaukee, hardly know her, & responses to names
@client.event
async def on_message(message):
    if message.author.bot:
        return
    arr = str.split(message.content)
    for i in range(len(arr)):
        if arr[i].casefold() == "i'm" or arr[i].casefold() == "im":
            channel = message.channel
            await channel.send("Hi " + arr[i + 1] + ", im botlionis")

    if "msoe" in message.content.casefold() or "milwaukee" in message.content.casefold():
        channel = message.channel
        await channel.send(":(")

    for i in range(len(arr)):
        if arr[i].casefold().endswith("er"): 
            channel = message.channel
            await channel.send(arr[i] + "? I hardly know her!")

    for i in range(len(arr)):
        if arr[i].casefold() == "dan" or arr[i].casefold() == "tulio" or \
            arr[i].casefold() == "daniel" or arr[i].casefold() == "malcolm" or \
            arr[i].casefold() == "aj" or arr[i].casefold() == "miguel":
            channel = message.channel
            await channel.send(arr[i] + "? " + random.choice(client.responsesToNames))

    await client.process_commands(message)

# check active functions
@client.command(name = 'functions')
async def functions(context):
    functionEmbed = discord.Embed(title = "Documentation")
    functionEmbed.add_field(name = "Functions", value = "!joke, !image, !react, !excuse, !hmm, !quoteadd, !quote, !chat, + responds to 'i'm', '-er', 'msoe', 'milwaukee', & certain names", inline = False)
    functionEmbed.set_footer(text = "Version 1.4.0")
    await context.message.channel.send(embed = functionEmbed)

# excuses
client.excuses = ["my moms making salmon", "my house blew up", "my house was destroyed in a tornado",
                    "my wrists hurt", "im in bolivia", "im doing ^*$^@&^( today", "i'm gassed",
                    "i got work", "it's my bedtime", "my mom's calling", "im in uzbekistan",
                    "im tired af", "ive been drafted", "i havent slept in seven days"]
@client.command(name = 'excuse')
async def excuse(context):
    await context.message.channel.send(random.choice(client.excuses))

#jokes
client.jokes = ["Whats the best thing about Switzerland? I dont know, but the flag is a big plus.", 
                "Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?",
                "What do you call a man with no body and no nose? Nobody knows",
                "What's the similarity between me and a muskellunge? We both want to consume Dua Lipa's flesh!",
                "What does a nosy pepper do? Gets jalapeño business!", "How does Moses make tea? He brews.",
                "Why don’t math majors throw house parties? Because you should never drink and derive.",
                "What's 9 + 10? 21!", "A skeleton walks into a bar and asks for a beer and a mop",
                "The rich get richer and the Dan gets Danner", "Said your father, was a great man",
                "What do you call a cow with no legs? Ground beef!", "What do you call a surfer cow? Cowabunga!",
                "Whats brown and sticky? A stick", "What is red and smells like green paint? Red paint",
                "What do you call a guy named Tulio? Tulio!", "What do you call a man? His name",
                "What's red and hurts your teeth? A brick", "Six thirty is the best time, hands down",
                "What's the difference between a piano, a fish, and a hanger? You can tune a piano but you can't tune a fish. I knew you'd get hung up on the hanger"]
@client.command(name = 'joke')
async def joke(context):
    await context.message.channel.send(random.choice(client.jokes))

#rickroll
@client.command(name = 'hmm')
async def hmm(context):
    rickroll = discord.Embed(title = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    await context.message.channel.send(embed = rickroll)    

#send random blue emoji as a reaction
client.react = [";).jpg", "ah.jpg", "ahh.jpg", "bruh.jpg", "cool.jpg", "fear.jpg", "grr.jpg",
                    "happy.jpg", "munch.jpg", "smile.jpg", "uh.jpg", "uhh.jpg", "wow.jpg",
                    "yawn.jpg", "yum.jpg", "zoom.jpg"]

@client.command(name = 'react')
async def react(context):
    await context.message.channel.send(file = discord.File(random.choice(client.react)))

#send random images
client.images = ["1.png", "2.jpg", "3.jpg", "4.PNG", "5.png", "6.png", "7.PNG", "8.png", "9.PNG",
                "10.PNG", "11.jpg", "12.png", "13.jpg", "14.png", "15.jpg", "16.png", "17.png",
                "18.PNG", "19.PNG", "20.png", "21.png", "22.jpg", "23.jpg", "24.jpg", "25.jpg",
                "26.png", "27.png", "28.PNG", "29.jpg", "30.jpg", "31.jpg", "32.jpg", "33.jpg",
                "34.jpg", "35.jpg", "36.png", "37.jpg", "38.jpg", "39.png", "40.png", "41.jpg",
                "42.png", "43.png", "44.png", "45.png", "46.png", "47.png", "48.jpg", "49.jpg",
                "50.PNG", "51.PNG", "52.png", "53.jpg", "54.jpg", "55.jpg", "56.png", "57.png",
                "58.jpg", "59.png", "60.jpg", "61.jpg", "62.jpg", "63.png", "64.jpg", "65.PNG",
                "66.png", "67.PNG", "68.PNG"]
@client.command(name = 'image')
async def image(context):
    await context.message.channel.send(file = discord.File(random.choice(client.images)))

#Quote list and recitation
client.quotelist = []
@client.command(name = 'quoteadd')
async def quoteadd(context, *, item):
    client.quotelist.append(item)
    await context.message.channel.send("Quote added.")

@client.command(name = 'quote')
async def quote(context):
  await context.message.channel.send(random.choice(client.quotelist))

#chat with the bot
client.firstResponses = ["What's your favorite color?", "Where do you go to college?", "Where do you live?",
                        "What's up?", "How is your day?", "Tell me something", "Tell me something funny",
                        "What's your favorite TV show?", "What's your favorite movie?", 
                        "What's your favorite band or musician?"]
client.secondResponses = ["I hate that", "I love that also", "I am incapable of understanding",
                        "What are you talking about?", "Are you insane?", "Bro?", "You good bro?",
                        "That's wacky man", "I am a big fan", "I know not of what you speak",
                        "Wtf", "Okay", "I guess so", "Are you sure?", "Chill.", "Big fan", "wow!",
                        "Solid choice", "Tulio type beat right there", "Goo goo gaa gaa", "Nice",
                        "I gotchu", "DWHAUDGWDJHWD", "AAAAAAAAAAHHHHH", "Wacko!"]
client.thirdResponses = ["I've had it with you", "That's enough", "Shut up", "I'm done",
                        "Finally some facts being spat", "I see how it is", "Goo goo gaa gaa",
                        "I'm going home", "Take me home", "Alright buddy", "Alright buster",
                        "ooookay I see how it is", "I gotta go", "My moms calling", "It's my bedtime"]
@client.command(name = 'chat')
async def chat(context):
    await context.message.channel.send("Hello, " + context.author.display_name)
    await context.message.channel.send(random.choice(client.firstResponses))

    def check(m):
        return context.author.bot == False and m.channel == context.message.channel

    msg = await client.wait_for("message", check=check)
    await context.message.channel.send(random.choice(client.secondResponses))

    def check(m):
        return context.author.bot == False and m.channel == context.message.channel

    msg = await client.wait_for("message", check=check)
    await context.message.channel.send(random.choice(client.thirdResponses))
    

client.run('OTgzMTgyMjY2NDgwMDc4ODQ4.GOfXft._clNk8gRVHF8wykUiB_d_jTDZD5vZbYOPeT0QA')