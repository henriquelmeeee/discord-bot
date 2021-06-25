import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='!', case_insensitive='True')


from utilitarios import *

@client.event
async def on_ready():
    l()
    msg('Bot online!')
    msg(f'Nome do bot: {client.user.name}')
    msg(f'ID do bot: {client.user.id}')
    l()


async def on_disconnect():
    msg('Bot desconectado!')


@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!moeda'):
        await message.channel.send(f'Resultado foi {random.choice(["cara", "coroa"])}!')
    elif message.content.startswith('!cara'):
        await message.channel.send(f'Resultado foi {random.choice(["cara", "coroa"])}!')
    elif message.content.startswith('!coroa'):
        await message.channel.send(f'Resultado foi {random.choice(["cara", "coroa"])}!')
    else:
        pass
    if message.content.startswith('emoji'):
        await message.channel.send('Adicionando emoji...')
        await message.add_reaction("⬆")
        pass
    else:
        pass
    if message.content.startswith('!verificarbot'):
        await message.channel.send('O bot <@ID> está disponível!\n'
        f'Nome do bot: {client.user.name}\n'
        f'ID do bot: {client.user.id}\n'
        'Use "!help" para ajuda.')
    else:
        pass


client.run\
    ('token')
