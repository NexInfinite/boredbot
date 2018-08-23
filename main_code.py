import discord
import random
import shlex
from tokens import *
from sql_commands import *
import os

msg = ''

client = discord.Client()

bordem_messages = ['Eat some food', 'Dab on them haters', 'Watch a movie', "Watch nex's stream",
                   'Do some launchpadding', "Wouldn't you like to know weather boi", "play a game", 
                   "yOu NeEd To WoKe", "watch tv", "play OUTSIIIIIIDE", "play a boardgame", 
                   "watch small boi's stream Kappa", "talk", "Buy some bored squad merch (no plugs)",
                   "http://nexinfinite.stream/projects.html *cough* *cough*, how did that get there", 
                   "play some rocket league"]

commands = '^bored', '^list_bored'


@client.event
async def on_message(message):
    global msg
    if message.author == client.user:
        return

    if message.content.lower().startswith('^help'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user} the commands are ```{", ".join(commands)}```'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user}, {random.choice(bordem_messages)}.'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^list_bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user} the bored messages are: ```{", ".join(bordem_messages)}```'
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('--------------')
    await client.change_presence(game=discord.Game(name='^help'))

client.run(os.getenv('TOKEN'))
