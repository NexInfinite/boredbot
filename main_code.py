import discord, random, shlex, os, time, requests, json, re
from tokens import *
from sql_commands import *

msg = ''

client = discord.Client()

bordem_messages = ['Eat some food.', 'Dab on them haters.', 'Watch a movie.', "Watch nex's stream.",
                   'Do some launchpadding?',
                   "Wouldn't you like to know weather boi!", "play a game", "yOu NeEd To WoKe", "watch tv!",
                   "play OUTSIIIIIIDE",
                   "play a boardgame"]

commands = ['^bored', '^list_bored', '^youtube_search', '^testing']
commands_desc = ['This command picks a random message from a list',
                 'This command will give you a list of all the responses from the ^bored command.',
                 'This command will search youtube for a video with your keyword and will give you the videso found (Broken right now)',
                 'Yeah this command is just for me lolem']

@client.event
async def on_message(message):
    global msg

    if message.author == client.user:
        return

    if message.content.lower().startswith('^help'):
        user = '{0.author.mention}'.format(message)
        commands_split = "/n".join(commands)
        embed = discord.Embed(title="Commands", color=0x4E71F0)
        for i in range(len(commands)):
            embed.add_field(name=f"{commands[i]}", value=f'{commands_desc[i]}', inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('^bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user}, This is what you can do to not be bored: {random.choice(bordem_messages)}'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^list_bored'):
        user = '{0.author.mention}'.format(message)
        msg = f'{user} the bored messages are: ```{", ".join(bordem_messages)}```'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('^testing'):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await client.send_message(message.channel, embed=embed)

    #if message.content.lower().startswith('^youtube_search'):
    #    user = '{0.author.mention}'.format(message)
    #    split_message = shlex.split(message.content)
    #    api_key = DEVELOPER_KEY
    #    joined_message = ' '.join(split_message[1:])
    #    search_text = joined_message.split(', ')
    #    finished = 0
    #    if len(search_text) < 2:
    #        msg = f'{user} UR A FUCKING NOOB, U FORGOT TO ADD THE COMMA :ok_hand: Do this ```^youtube_search {joined_message}, (INSERT DUMBASS NUMBER HERE)```'
    #        await client.send_message(message.channel, msg)
    #    elif int(search_text[1]) <= 5:
    #        msg = f'{user} searching......... (This may take a while)'
    #        await client.send_message(message.channel, msg)
    #        search = requests.request('get', f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={search_text[1]}&q={search_text[0]}&type=video&key={api_key}')
    #        json_search = search.text
    #        youtube_url = json.loads(json_search)
    #        items = youtube_url['items']
    #        list = []
    #        if len(search_text) > 1:
    #            if items:
    #                for i in range(int(search_text[1])):
    #                    items_0 = items[i]
    #                    id = items_0['id']
    #                    video_id = id['videoId']
    #                    snippet = items_0['snippet']
    #                    title = snippet['title']
    #                    link_final = f'https://www.youtube.com/watch?v={video_id}'
    #                    list.append(f"[{i+1}] {title}: \n {link_final}")
    #                    finished = 1
    #            else:
    #                msg = f'{user} Sorry no results!'
    #                await client.send_message(message.channel, msg)
    #    else:
    #        msg = f'{user} No more than 5 results'
    #        await client.send_message(message.channel, msg)
    #
    #    if finished == 1:
    #        new_line_list = '\n \n'.join(list)
    #        embed = discord.Embed(title="", color=0xc00707)
    #        embed.add_field(name='Youtube search results:', value=f'{new_line_list}', inline=False)
    #        await client.send_message(message.channel, embed=embed)
    #        finished = 0


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('--------------')
    await client.change_presence(game=discord.Game(name='^help - beta'))

client.run(TOKEN)

