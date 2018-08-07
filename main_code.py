import discord
import random
import shlex
from tokens import *
from sql_commands import *

TOKEN = TOKEN

msg = ''

client = discord.Client()

bordem_messages = ['Eat some food.', 'Dab on them haters.', 'Watch a movie.', "Watch nex's stream.", 'Do some launchpadding?', "Wouldn't you like to know weather boi!"]

@client.event
async def on_message(message):
    global msg
    if message.author == client.user:
        return

    if message.content.lower().startswith('^bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user}, This is what you can do to not be bored: {random.choice(bordem_messages)}'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^addmsg'):
        user = '{0.author.mention}'.format(message)
        role_names = [role.name for role in message.author.roles]
        if "leader" in role_names:
            print('working!!!!!!!!!!')
            #split_message = shlex.split(message.content)
            #print(split_message[1:])
            #if len(split_message) < 2:
                #msg = f'```ERROR, use: ^boredadd XXXXXXXXXXX. The XXXXX must be replaced with your own message!```'
                #await client.send_message(message.channel, msg)
            #else:
                #response = insert_msg(
                    #message_given=split_message[1:]
                #)
                #if response == 0:
                    #msg = f'{user} successfully added the message *{" ".join(split_message[1:])}* to the database!'
                    #await client.send_message(message.channel, msg)
                #elif response == 1:
                    #msg = f'{user} the response {" ".join(split_message[1:])} is already in the database, try another response'
                    #await client.send_message(message.channel, msg)
        else:
            print('nein')
            #msg = f'{user}, this command is down rn. I am working on it and cant have people doing stuff with it.'
            #await client.send_message(message.channel, msg)
            #print(message.author)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('--------------')
    msg = f'```Hello, Im Bored bot v1.0.5, How bored are u?```'
    await client.send_message(client.get_channel('447354418250121216'), msg)
    await client.change_presence(game=discord.Game(name='^help'))

client.run(TOKEN)
