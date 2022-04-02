import mytokens
import discord
import random
from discord.ext import commands
import requests

client = discord.Client()
client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.event #event to display when bot is running
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    #prints in terminal

@client.event #event for random commands
async def on_message(message): #to log channel messages in terminal

    if not message.guild: #will ignore messages sent in DMs
        pass 
    else:
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

@client.command() #clear command
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount + 1) #use +1 to also delete the $clear message

@client.command() #ping command
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms' )

@client.command() #kick command
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason) 

@client.command() #ban command
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason) 
    await ctx.send(f'Banned {member.mention}')

@client.command() #unban command
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
 
@client.command() #embed command
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='This is a footer.')
    embed.set_image(url='https://cdn.discordapp.com/attachments/667900649664675857/958242500940795944/IMG_4999.jpg')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/667900649664675857/953754912813101106/IMG_4972.jpg?width=556&height=676')
    embed.set_author(name='Author Name',
    icon_url= 'https://mtv.mtvnimages.com/uri/mgid:ao:image:mtv.com:62307?quality=0.8&format=jpg&width=1440&height=810&.jpg')
    embed.add_field(name='Field Name', value='Field Value', inline= False)

    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blurple()
    )

    embed.set_author(name='Help')
    embed.add_field(name=' ping', value='Returns "Pong!"', inline = False)
    embed.add_field(name=' clear [value]', value='Deletes messages accouting to amount specified, otherwise will delete 100 messages automatically', inline = False)
    embed.add_field(name=' kick [@user]', value='Kicks user from sever. Use @[user] after the kick command to kick a specific user.', inline=False)
    embed.add_field(name=' ban [@user]', value='Bans user from sever.', inline=False)
    embed.add_field(name=' ban [@user]', value='Unbans user from sever. Be sure to use @user to unban them.', inline=False)


    await author.send(embed=embed)

client.run(mytokens.TOKEN) #runs on_message definition  