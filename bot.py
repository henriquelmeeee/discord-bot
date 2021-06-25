import discord, time, random
from discord.ext import commands

def msg(msg):
    print(msg)

client = commands.Bot(command_prefix = "!", case_insensitive=True)

@client.event
async def on_ready():
    msg('BOT ON!')
    msg(client.user.name)
    msg(client.user.id)
async def on_disconnect():
    msg('O bot se desconectou!')


@client.command()
async def teste(ctx):
    await ctx.send('Olá!')

@client.command()
async def meuNome(ctx):
    while True:
        if ctx.author == 'test':
            await ctx.send(f'Seu nome é {ctx.author}!')
            print('Mensagem enviada com sucesso, quebrando repetição..')
            break
        elif ctx.author == 'test2':
            await ctx.send(f'Seu nome é {ctx.author}!')
            print('Mensagem enviada com sucesso, quebrando repetição...')
            break
        else:
            n = 0
            msg = 0
            while n < 11:
                await ctx.send(f'Seu nome não é nem test nem test2.')
                print('Mensagem enviada com sucesso!')
                n = n + 1
                if n >= 10:
                    await ctx.send('Repetição finalizada.')
                    print(f'Repetição do usuário {ctx.author} finalizada.')
                    break
                time.sleep(1)
                msg = msg + 1
                await ctx.send(f'Mensagem {msg} enviada!')

@client.command()
async def rodardado(ctx, numero):
    try:
        rand = random.randint(1, int(numero))
        await ctx.send(f'Entre 1 à {numero}, o programa escolheu {rand}!')
        print('Sucesso!')
    except (ValueError, TypeError):
        print('Valor errado, digitação errada')
        await ctx.send('Você deve inserir um número inteiro.')
    except:
        print('Erro desconhecido')
        await ctx.send('*BOT TRISTE* Um erro desconhecido ocorreu!')

@client.command()
async def testarvariavel(ctx):
    try:
        a = 1
        await ctx.send(f'O valor é {a}!')
        await ctx.send(f'O valor é {b}!')
    except Exception as erro:
        await ctx.send('Ocorreu um erro com a variável B. Contate o desenvolvedor.')
        print(erro)


@client.command()
async def acertarNum(ctx, num):
    numrand = random.randint(1, 1)
    await ctx.send(f'Número escolhido: {numrand}')
    try:
        print(
            numrand
        )
        if numrand != num:
            await ctx.send('Você errou!')
        else:
            await ctx.send('Você acertou!')
    except Exception as erro:
        await ctx.send('Algo aconteceu!')
        print(erro)
    finally:
        pass

@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name

    if(author == 'SEU BOT'):
        return

    if(content == 'bom dia' and channel.name == 'bom-dia'):
        await channel.send(f"Bom dia, {message.author.mention}")

@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name

    if (author == client.user):
        return

    if (content == '!gerarnumero'):
        await channel.send(f'O número randômico gerado foi {random.randint(1, 1000)}!')

    else:
        return



@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name

    if (author == 'SEU BOT'):
        return

    if (content == '!help'):
        embed = discord.Embed(

            title='Título',
            description='Descrição',
            colour=discord.Colour.blue()

        )

        embed.set_author(name='Ajuda',
                         icon_url='https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')
        embed.set_thumbnail(url='https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')
        embed.set_image(url='https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')

        await channel.send(embed = embed)

    else:
        return

@client.command()
async def enviarembed(ctx):
    embed = discord.Embed(

        title = 'Título',
        description = 'Descrição',
        colour = discord.Colour.blue()

    )


    embed.set_author(name='Teste', icon_url = 'https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')
    embed.set_thumbnail(url='https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')
    embed.set_image(url='https://imagepng.org/wp-content/uploads/2019/12/check-icone-scaled.png')


    await ctx.send(embed = embed)
    print('Embed enviado com sucesso!')








client.run\
    ('SEU TOKEN')
