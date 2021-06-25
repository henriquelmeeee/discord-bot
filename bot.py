import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='!', case_insensitive='True', intents=discord.Intents.all())

from utilitarios import *

@client.event
async def on_ready():
    l()
    msg('Bot online!')
    msg(f'Nome do bot: {client.user.name}')
    msg(f'ID do bot: {client.user.id}')
    l()


@client.command()
async def moeda(ctx, caracoroa):
    embed = discord.Embed(

        title='Cara ou Coroa',
        description=f'A moeda escolhida foi: {random.choice(["CARA", "COROA"])}\n'
                    f'e você escolheu: {caracoroa.upper()}',
        colour=discord.Colour.blue()

    )

    embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
    await ctx.send(embed = embed)

client.run\
    ('TOKEN')
