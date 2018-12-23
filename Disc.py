import discord
import asyncio
from discord.ext import commands
import time
client = discord.Client()
comand = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    print(str(message.author)+" Said:"+str(message.content))
    
    
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
     
    if message.content.startswith('!T') or message.content.startswith('!TGAY') or message.content.startswith('t'):
        channel = message.channel
        async for message in client.logs_from(channel, limit=1):
            messages = (message)
        await client.delete_message(messages)
        with open('gay.jpg', 'rb') as f:
            for x in range(0,10):
                await client.send_file(message.channel, f)
                time.sleep(0.5)
            x = 0


@comand.command(pass_context = True)
async def spam(ctx, amount = 10):
    channel = ctx.message.channel
    async for message in client.logs_from(channel, limit=1):
        messages = (message)
    await client.delete_message(messages)
    for x in range(0, int(amount)):
        with open('truekys.gif', 'rb') as f:
            await client.send_file(message.channel, f)
        await asyncio.sleep(0.5)
    x = 0




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTI0Mzc4Nzc5OTEzNjgyOTU0.Dv7J7Q.LxiyUEQi4NbSzGHGH3jeJUKLXHw')
