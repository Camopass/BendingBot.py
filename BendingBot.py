import discord
import asyncio
import sqlite3

conn = sqlite3.connect('BendingBotUsers.db')


from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound
prefix = '>'
client = commands.Bot(command_prefix = prefix)
yemoji = '\U0001F1FE'
nemoji = '\U0001F1F3'
canaccept = 0


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('>help for a list of commands')) #Shows a status update for whenever the bot is ready
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    NMembersChannel = client.get_channel(741069132073533452)
    await NMembersChannel.send(f'Hello, {member.mention}! Welcome to the avatar fan server! Please make sure to read the rules!')


@client.command(description= 'Finds the level required for a certain number of abilities.')
async def findlvl(ctx, lvl: int):
    x = lvl * 5
    await ctx.send(f'For {lvl} abilities, you need {x + 10} levels.')

@client.command(description= 'Some context')
async def info(ctx):    #Provides info on the bot
    await ctx.send(f'Hello {ctx.author.mention}, I am Korra, the probending battle bot. I am still under development by <@!379307644730474496>, please go to #bending-bot-dev to ask questions or give suggestions.')


@client.command(description='Challenge another user')    #challenges! yay!
async def challenge(ctx, person2: discord.Member):
    logchannel = client.get_channel(754056853100691476)
    global opponent
    if ctx.author == person2:
        await ctx.send('You can`t challenge yourself!')
    else:
        opponent = person2
        await logchannel.send(f'challenge between {ctx.author} and {opponent} proposed!')
        message = await ctx.send(f'{person2.mention}! {ctx.author.mention} has challenged you to a duel! You have 90 seconds to accept.')
        await message.add_reaction(yemoji)
        await message.add_reaction(nemoji)
        channel = ctx.channel
        def check(reaction, user):
            global opponent
            return str(reaction.emoji) == yemoji and user == opponent
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=90.0, check=check)
        except asyncio.TimeoutError:
            await channel.send(f'Challenge between {ctx.author.mention} and {opponent.mention} cancelled')
            await logchannel.send(f'challenge between {ctx.author} and {opponent} cancelled')
        else:
            print(f'challenge between {ctx.author} and {opponent} accepted')
            await channel.send('Challenge accepted!')
            await logchannel.send(f'challenge between {ctx.author} and {opponent} accepted')
        challenger = ctx.author

@client.command(name= 'hi')
async def hi(ctx):
    embed=discord.Embed(title='Hello', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', description='Is it me youre looking for?', color=0x5800db)
    embed.add_field(name='Me', value='0', inline='False')
    embed.set_footer(text='Helloooo')
    await ctx.send(embed=embed)

client.run('NzUwNDY4ODE2NTg0MTc5ODAy.X06-jA.JnNzuITfZc3009RIH6c79iBHOeo')
