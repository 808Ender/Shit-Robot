import discord
from discord.ext import commands
client = discord.Client()
commandz = commands.Bot(command_prefix = '!')
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
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






@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTI0Mzc4Nzc5OTEzNjgyOTU0.DvuOHQ.A87HvGhelbQLo_KzlTbA0RUlDTQ')