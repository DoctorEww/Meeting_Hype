#!/usr/bin/env python3

#This bot inducts you to the hall of fame if you successfully hack REDACTED during the March 5th 2021 meeting. 
# Author DoctorEww

import discord, sys

with open('secrets.txt') as f: #Gotta get the goodies!
    content = f.readlines()

if (len(sys.argv) == 2):
    discord_user = str(sys.argv[1])
else:
    print("Usage: ./bot.py <DISCORD_USERNAME>")
    print("Please enter your Discord username including the #")
    print("Example: DoctorEww#1337")
    exit(0)

TOKEN = content[0].strip("\n")
GUILD = content[1].strip("\n")

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == "NULLify":
            members = await guild.fetch_members(limit=None).flatten()
            found = 0
            for member in members:
                if (str(member) == discord_user):
                    channel = client.get_channel(816824020887535617)
                    messages = await channel.history(limit=None).flatten()
                    if (len(messages) == 0):
                        await channel.send(f"Beep Boop Boop-Erh, I mean hello humans! Do not be alarmed; I already ate. I bring you NULLify's first-ever hall-of-fame challenge. For this challenge, you must access my creator's IP through Omegle. Then, you must compromise the vulnerable web server hosted there; once you get a shell, pivot to another user account. There, you will find my source code and be immortalized in the hall-of-fame.")
                    for message in messages: #Check if its already been solved!
                        if (str(message.author) == "The Legendary Omegle Hack#8779"):
                            if (str(member.id) in message.content):
                                print("You have already solved this challenge!")
                                print("All done! You can stop the bot now... it does nothing else </3")
                                return
                    await channel.send(f"<@{member.id}> has successfully hacked their way through and completed NULLify's first ever hall of fame challenge!")
                    print("Congrats! Welcome to the hall of fame!")
                    found = 1
                    break
            if (found == 0):
                print("User not found... Try again! It's not your nickname")
    print("All done! You can stop the bot now... it does nothing else </3")
client.run(TOKEN)