# bot.py
import os, random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from bot.zizBot import ziz


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    ziz().hello()
    print(f'{bot.user.name} has connected to Discord!')
    print(f"Guilds : {bot.guilds}")
    for guild in bot.guilds:
        print(f"Name : {guild.name}")

        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    print(member)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message, ):
    if 'fuck' in message in message.content.lower():
        await message.channel.send("fuck toi-meme")



@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)

    await ctx.send(response)


@bot.command(name='nba')
async def nba(ctx):
    nba = ziz().NBA()
    
    await ctx.send(nba)


# client.run(TOKEN)
bot.run(TOKEN)