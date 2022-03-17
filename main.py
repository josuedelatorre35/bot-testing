import mytokens
import discord
import random
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    #prints in terminal

@client.event
async def on_message(message):
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'({channel}) {username}: {user_message}')
    #messages in print statement will be logged in terminal

    if message.author == client.user:
        return #prevents bot from repsonding to itself
    
    if message.channel.name == 'bot':
        if user_message.lower() == '$hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '$bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '$random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)

    if user_message.lower() == '$anywhere':
        await message.channel.send('This can be used anywhere!')
        return
    await client.process_commands(message)

@client.command() 
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount + 1) #use +1 to also delete the $clear message


client.run(mytokens.TOKEN) #runs on_message definition  
