import discord
import random
import shlex
from tokens import *
from sql_commands import *
import os

msg = ''

client = discord.Client()

bordem_messages = ['Eat some food.', 'Dab on them haters.', 'Watch a movie.', "Watch nex's stream.", 'Do some launchpadding?',
                   "Wouldn't you like to know weather boi!", "play a game", "yOu NeEd To WoKe", "watch tv!", "play OUTSIIIIIIDE",
                   "play a boardgame", "listen to: agiauegbae LET THE GAMES BEGIN IS AMAZE"]

commands = '^bored', '^list_bored'

@client.event
async def on_message(message):
    global msg
    if message.author == client.user:
        return
    
    if message.content.lower().startswith('^help'):
        user = '{0.author.mention}'.format(message)
        split_message = shlex.split(message)
        if len(messgae) < 2:
            msg = f'{user} the commands are ```{commands}```'
            await client.send_message(message.channel, msg)
        if len(message) > 2:
            if split_message[1] == '^bored':
                msg = f'{user}, just do ^bored to get a random answer from the list'
                await client.send_message(message.channel, msg)
            if split_message[1] == '^list_bored':
                msg = f'{user}, ^list_bored gives you a list of all the answers for ^bored'
                await client.send_message(message.channel, msg)
          
      
    if message.content.lower().startswith('^bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user}, This is what you can do to not be bored: {random.choice(bordem_messages)}'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^list_bored'):
        user = '{0.author.mention}'.format(message)
        split_message = shlex.split(message)
        msg = f'{user} the bored messages are: ```{bordem_messages}```'
        await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('--------------')
    msg = f'```Hello, Im Bored bot v1.0.5, How bored are u?```'
    await client.send_message(client.get_channel('412723545316261890'), msg)
    await client.change_presence(game=discord.Game(name='^help'))

client.run(os.getenv('TOKEN'))
