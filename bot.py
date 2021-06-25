import sqlite3
import time

import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='!', case_insensitive='True', intents=discord.Intents.all())

banco = sqlite3.connect('banco.db')

from utilitarios import *

@client.event
async def on_ready():
    l()
    msg('Bot online!')
    msg(f'Nome do bot: {client.user.name}')
    msg(f'ID do bot: {client.user.id}')
    l()


@client.command(aliases=['coroa', 'cara', 'caraoucoroa', 'jogarmoeda', 'coroaoucara'])
async def moeda(ctx, caracoroa):
    res = random.choice(["cara", "coroa"])
    caracoroa = caracoroa.lower()
    if caracoroa == 'cara' or caracoroa == 'coroa':
        if caracoroa == 'cara':
            if res == 'cara':
                embed = discord.Embed(

                    title='Cara ou Coroa',
                    description=f'A moeda escolhida foi: {res.upper()}\n'
                                f'e você escolheu: {caracoroa.upper()}\n'
                                f'Você ganhou!',
                    colour=discord.Colour.blue()

                )

                embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
                await ctx.send(embed = embed)
            elif res == 'coroa':
                embed = discord.Embed(

                    title='Cara ou Coroa',
                    description=f'A moeda escolhida foi: {res.upper()}\n'
                                f'e você escolheu: {caracoroa.upper()}\n'
                                f'Você perdeu...',
                    colour=discord.Colour.blue()

                )

                embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
                await ctx.send(embed=embed)
        elif caracoroa == 'coroa':
            if res == 'coroa':
                embed = discord.Embed(

                    title='Cara ou Coroa',
                    description=f'A moeda escolhida foi: {res.upper()}\n'
                                f'e você escolheu: {caracoroa.upper()}\n'
                                f'Você ganhou!',
                    colour=discord.Colour.blue()

                )

                embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
                await ctx.send(embed=embed)
            elif res == 'cara':
                embed = discord.Embed(

                    title='Cara ou Coroa',
                    description=f'A moeda escolhida foi: {res.upper()}\n'
                                f'e você escolheu: {caracoroa.upper()}\n'
                                f'Você perdeu...',
                    colour=discord.Colour.blue()

                )

                embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
                await ctx.send(embed=embed)
    else:
        embed = discord.Embed (
            title='',
            description='Você deve digitar cara ou coroa após o comando!'

        )
        await ctx.send(embed = embed)
        l()
        print('Usuário digitou incorretamente.')
        print(f'Usuário digitou "{caracoroa}" e devia ser ou cara ou coroa!')
        l()

@client.command(aliases=['source', 'source-code', 'botsource'])
async def github(ctx):
    embed = discord.Embed(

        title='Meu GITHUB',
        description='https://github.com/henriquelmeeee/discord-bot/blob/main/bot.py'
    )
    await ctx.send(embed = embed)


saldo = 0

@client.command()
async def economia(ctx):
    await ctx.send(f'Seu saldo é {saldo}.')
    await ctx.send('A economia ainda não está disponível.')


@client.command(aliases=['a', 'suporte'])
async def ajuda(ctx):
    embed = discord.Embed(

        author = {
                'name': 'Some name',
                'url': 'https://discord.js.org'
        },
        title='Suporte',
        description='teste'

    )

    await ctx.send(embed = embed)


@client.command(aliases=['say'])
async def falar(ctx, *, mensagem=None):
    if mensagem is None:
        await ctx.send('Informe um valor válido.')
    else:
        await ctx.message.delete() #deletar mensagem do bot
        await ctx.send(mensagem)


client.run\
    ('TOKEN')
