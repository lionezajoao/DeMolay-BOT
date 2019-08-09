import discord
import asyncio

arq = open("backup.txt", "a+")

client = discord.Client()

status = "online"

@client.event
async def on_ready():
    print(status.upper())

@client.event

async def on_message(message):
    if message.content.lower().startswith("!welcome"):
        await message.channel.send("**```Bem vindo ao canal do Gabinete Estadual da Liderança Juvenil do Estado do Rio de Janeiro! \nPor favor, junto com '!save', nos fale seu nome, cid, capítulo e cargo.```**")
        
    if message.content.lower().startswith("!save"):
        msg = message.content.replace("!save ", "")
        arq.write(msg+"\n\n")

client.run("TOKEN")

arq.close()
