# bot.py
import os, random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from bot.zizBot import ziz
from NBA.NBA import NBA

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

bot = commands.Bot(command_prefix='-')


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


@bot.event
async def on_member_join(member):
    print(member)
    await member.create_dm()
    await member.dm_channel.send(
        f'Sup {member.name}, On ma dit ca game ?'
    )


# @bot.event
async def on_message(message):
    print(f'message:{message.content}')

    i = 0 
    for word in message.content.split(' '):
        if 'bonjour' == word.lower():
            i += 1
        if 'ziz' == word.lower():
            i += 1
        if i == 2:
            await message.channel.send("Dze si majstore")
            break
        


@bot.command(name='998')
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
async def nba(ctx, args):
    print('nba')
    # nba = ziz().NBA(args)
    # await ctx.send(nba)
    print(f'args:{args}')
    await ctx.send(NBA(args))


# Exemple d'arguments
@bot.command(name='arg')
async def arg(ctx, args):

    for arg in args:
        print(args)



# client.run(TOKEN)
bot.run(TOKEN)