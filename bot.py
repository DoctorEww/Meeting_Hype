#This bot inducts you to the hall of fame if you successfully hack REDACTED during the March 5th 2021 meeting. 
# Author DoctorEww

import discord

with open('secrets.txt') as f: #Gotta get the goodies!
    content = f.readlines()
print("Please enter your Discord username including the #")
print("Example: DoctorEww#1337")
discord_user = input()
TOKEN = content[0].strip("\n")
GUILD = content[1].strip("\n")

client = discord.Client()
@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)
        if guild.name == "NULLify":
            members = await guild.fetch_members(limit=None).flatten()
            for member in members:
                if (str(member) == discord_user):
                    print(member.id)
                    channel = client.get_channel(816824020887535617)
                    messages = await channel.history(limit=None).flatten()
                    print(messages)
                    if (len(messages) == 0):
                        await channel.send(f"Beep Boop Boop-Erh, I mean hello humans! Do not be alarmed; I already ate. I bring you NULLify's first-ever hall-of-fame challenge. For this challenge, you must access my creator's IP through Omegle. Then, you must compromise the vulnerable web server hosted there; once you get a shell, pivot to another user account. There, you will find my source code and be immortalized in the hall-of-fame.")
                    for message in messages:
                        print(message.author)
                        if (str(message.author) == "The Legendary Omegle Hack#8779"):
                            if (str(member.id) in message.content):
                                print("You have already solved this challenge!")
                                break
                        await channel.send(f"<@{member.id}> has successfully hacked their way through and completed NULLify's first ever hall of fame challenge!")
                        print("Congrats! Welcome to the hall of fame!")
    
    print("All done!")
#user = await client.fetch_user("224366954096361472")
client.run(TOKEN)