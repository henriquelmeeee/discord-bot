# O código a seguir foi feito por um iniciante em Python e em bibliotecas Discord.py.

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


@client.event
async def on_member_join(member):
    guild = member.guild # Definindo "guild"
    canal = discord.utils.get(guild.channels, id=858396490262249522) # puxando o canal e o membro
    embed = discord.Embed(

        title = 'Novo membro!',
        description = f'Bem vindo, {member.mention}!\n'
                      f''

    )
    await canal.send(embed = embed)

@client.event
async def on_member_remove(member):
    guild = member.guild
    canal = discord.utils.get(guild.channels, id=858397258810654750)
    embed = discord.Embed(

        title = 'Até mais..',
        description = f'O usuário {member.mention} saiu!\n'
                      f'Sentiremos sua falta!\n'
                      f''

    )

    await canal.send(embed = embed)

@client.event
async def on_message(message):
    if 'scam' in message.content.lower():
        await message.delete()
        mensagem = 'Você não pode enviar isso aqui, engraçadinho!'
        await message.channel.send(mensagem)



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
                msg = await ctx.send(embed = embed)
                await msg.add_reaction('✔')
            elif res == 'coroa':
                embed = discord.Embed(

                    title='Cara ou Coroa',
                    description=f'A moeda escolhida foi: {res.upper()}\n'
                                f'e você escolheu: {caracoroa.upper()}\n'
                                f'Você perdeu...',
                    colour=discord.Colour.blue()

                )

                embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/ja/jaqueroque/cara-ou-coroa.png')
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
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
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('✔') # Adicionar reação
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


@client.command(aliases=['a', 'suporte'])
async def ajuda(ctx):
    embed = discord.Embed(

        title='Suporte',
        description='teste'

    )

    await ctx.send(embed = embed)


@client.command(aliases=['say'])
async def falar(ctx, *, mensagem=None):
    if ctx.author.guild_permissions.administrator:
        if mensagem is None:
            await ctx.send('Informe um valor válido.')
        else:
            await ctx.message.delete() #deletar mensagem do usuario
            await ctx.send(mensagem)
    else:
        await ctx.send('Você não tem permissão para executar este comando.')


@client.command(aliases=['credits', 'donodobot', 'botdono', 'donobot'])
async def creditos(ctx):
    if ctx.author.id == 852634334909562910:
        embed = discord.Embed (

            title='Créditos',
            description='O dono do bot é <@852634334909562910>!\n'
                        'Você é o dono!'

        )
        await ctx.send(
            embed = embed
        )
    else:
        embed = discord.Embed(

            title='Créditos',
            description='O dono do bot é <@852634334909562910>!'

        )
        await ctx.send(
            embed=embed
        )


@client.command(aliases=['registrar'])
async def registro(ctx, member: discord.Member=None, opcao: str=None):
    if ctx.author.guild_permissions.administrator:
        try:
            if member is None:
                await ctx.send('Você precisa mencionar algum usuário!')
            elif opcao is None:
                await ctx.send('Você precisa selecionar uma opção.\n'
                               'Digite "!veropcoes" para ver os cargos disponíveis.')
            else:
                if opcao == 'apoiador':
                    apoiador = discord.utils.get(ctx.guild.roles, id=851835455858671646)
                    await member.add_roles(apoiador)
                    msg = await ctx.send('Cargo "Apoiador" foi setado com sucesso!')
                    await msg.add_reaction('✔')
        except Exception as erro:
            print(erro)
            await ctx.send(f'O seguinte erro ocorreu: "{erro}"')
    else:
        await ctx.send('Você não tem permissão para executar este comando.')

@client.command(aliases=['removerole'])
async def removercargo(ctx, member: discord.Member=None, opcao: str=None):
    if ctx.author.guild_permissions.administrator:
        try:
            if member is None:
                await ctx.send('Você precisa mencionar algum usuário!')
            elif opcao is None:
                await ctx.send('Você precisa selecionar uma opção.\n'
                               'Digite "!veropcoes" para ver os cargos disponíveis.')
            else:
                if opcao == 'apoiador':
                    apoiador = discord.utils.get(ctx.guild.roles, id=851835455858671646)
                    await member.remove_roles(apoiador)
                    msg = await ctx.send('Cargo "Apoiador" foi removido com sucesso!')
                    await msg.add_reaction('✔')
        except Exception as erro:
            print(erro)
            await ctx.send(f'O erro "{erro}" ocorreu!')
    else:
        await ctx.send('Você não tem permissão para executar este comando.')

@client.command(aliases=['banir', 'punir', 'punish'])
async def ban(ctx, member: discord.Member=None, motivo: str=None):
    if ctx.author.guild_permissions.administrator:
        try:
            if member is None:
                await ctx.send('Você precisa informar um usuário!')
            elif motivo is None:
                if ctx.author.guild_permissions.manage_guild:
                    motivo = 'naoinformado'
                    pass
                else:
                    await ctx.send('Você precisa da permissão de gerenciar servidor para banir sem motivo.')
            else:
                await member.ban()
                embed = discord.Embed(

                    title='BANIMENTO',
                    description=f'O membro "{member}" foi banido por "{ctx.author}"!'


                )
                await ctx.send(embed = embed)
                if motivo == 'naoinformado':
                    embed = discord.Embed(

                        description='Motivo: Não informado!'

                    )
                    await ctx.send(embed = embed)
                else:
                    embed = discord.Embed(

                        description=f'Motivo: {motivo}!'

                    )
                    await ctx.send(embed = embed)
        except Exception as erro:
            print(erro)
            await ctx.send(f'O seguinte erro ocorreu: "{erro}"')
    else:
        await ctx.send('Você precisa de permissão para executar este comando.')

@client.command()
async def expulsar(ctx, member: discord.Member=None, motivo=None):
    try:
        if member is None:
            await ctx.send('Você deve informar um usuário válido!')
        elif motivo is None:
            await ctx.send('Você deve informar um motivo!')
        else:
            await member.kick()
            print(f'{member} expulso')
            await ctx.send(f'O usuário {member.mention} foi expulso por {ctx.author.mention}!\n'
                           f'Motivo: "{motivo}"')
    except Exception as erro:
        print(erro)
        await ctx.send('Um erro ocorreu! Veja o console para mais informações.')


@client.command(alises=['clear', 'clearchat', 'limparchat', 'chatclear', 'chatlimpar', 'chatlimpo'])
async def limpar(ctx, numero=None):
    if ctx.author.guild_permissions.administrator:
        if numero is None:
            await ctx.send('Você deve informar quantas mensagens deletar!')
        else:
            await ctx.message.delete()
            await ctx.send('Mensagens deletadas!')
    else:
        await ctx.send('Você não tem permissão para executar este comando!')



client.run\
    ('TOKEN')
