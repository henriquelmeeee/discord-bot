import discord
import random
from discord.ext import commands

def msg(msg):
    print(msg)

client = commands.Bot(command_prefix='!', case_insensitive='True')


prefixo = '!'

@client.event
async def on_ready():
    msg('Bot online!')
    msg(f'Nome do bot: {client.user.name}')
    msg(f'ID do bot: {client.user.id}')

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


client.run\
    ('token')
