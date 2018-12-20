import discord
from discord.ext import commands
import time
client = discord.Client()
commandz = commands.Bot(command_prefix = '!')
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content.startswith('!hello'):
        msg = 'I hate you {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


    if message.content.startswith('!shortkys'):
        with open('short.gif', 'rb') as f:
            channel = message.channel
            async for message in client.logs_from(channel, limit=1):
                messages = (message)
            await client.delete_message(messages)
            await client.send_file(message.channel, f)


    if message.content.startswith('!longkys'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
        with open('long.gif', 'rb') as f:
            await client.send_file(message.channel, f)


    if message.content.startswith('!kys') or message.content.startswith('!kermitcide'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
        with open('truekys.gif','rb') as f:
            await client.send_file(message.channel, f)


    if message.content.startswith('!rev') or message.content.startswith('!reverse'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
        with open('rev.png', 'rb') as f:
            await client.send_file(message.channel, f)


    if message.content.startswith('!spam') or message.content.startswith('!s'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
        for x in range(0,100):
            with open('truekys.gif', 'rb') as f:
                await client.send_file(message.channel, f)
            time.sleep(0.5)
        x = 0







@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTI0Mzc4Nzc5OTEzNjgyOTU0.Dv2Q9Q.7YnNF35O02N6-RwmxgqLhIYza5E')
