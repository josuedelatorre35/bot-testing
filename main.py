import mytokens
import discord
import random
from discord.ext import commands
import requests

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

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms' )

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason) 

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason) 
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client.run(mytokens.TOKEN) #runs on_message definition  