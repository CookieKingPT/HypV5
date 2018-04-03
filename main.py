import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('--------------------------------')
    print('<HypixelPT> Iniciando')
    print('<HypixelPT> Verificando a versão')
    print('<HypixelPT> Concluido :)')
    print('<HypixelPT> Criado por ILUFan')
    print('--------------------------------')


@client.event
async def on_message(message):
    if message.content.lower().startswith('hy!help'):
        await client.send_message(message.channel, "Comandos em : https://lifebots.webnode.pt/hypixelpt")
    if message.content.lower().startswith('hy!info'):
        await client.send_message(message.channel, ":white_check_mark: HypixelPT V1.0 :white_check_mark: ")
    if message.content.lower().startswith('hy!store'):
        await client.send_message(message.channel, ":white_check_mark: https://store.hypixel.net/ :white_check_mark: ")
    if message.content.lower().startswith('hy!site'):
        await client.send_message(message.channel, ":white_check_mark: https://hypixel.net/ :white_check_mark: ")
    if message.content.lower().startswith('hy!stats'):
        await client.send_message(message.channel, ":white_check_mark: http://minecraft-mp.com/server-s81821 :white_check_mark: ")
    if message.content.lower().startswith('hy!vote'):
        await client.send_message(message.channel, ":white_check_mark: http://minecraft-mp.com/server/81821/vote/ :white_check_mark: ")



client.run('NDI5OTM0NzI2NjUzMDE4MTMx.DaI3nA.SxcuedQ36kHsY3Suh27y8Ab8WH4')
