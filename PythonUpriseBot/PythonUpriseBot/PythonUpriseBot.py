import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix= '!')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Uprise Bot Is Online')

@client.command()
async def ping(ctx):
    await ctx.send('Pong')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, self, user: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f'User {user} has been muted')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)




client.run('NzA1NDg2OTM5NjI0NTcwOTcz.Xsf_Ow.gzMWvathwRwqN9XCwc1me74r4mA')
