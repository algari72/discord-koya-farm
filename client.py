from log_events import *
import user.keytool as uk
import asyncio
import discord
import re

username = "skppy7#1176"

client = discord.Client()


@client.event
async def on_ready():
    printimed(f"Bot routine started succesfully as {client.user}")
    printimed("Sending initial commands...")
    await tasks('ddm',0)
    await tasks('fish',0)
    await tasks('daily',0)



@client.event
async def on_message(message):

    if message.author.__str__() == "Koya#1050":
        await analize_msg(message.content)

    elif message.author.__str__() == username:
        if message.content.startswith('/stop'):
            await message.channel.send('Routine is closing...')
            await client.close()
            printimed("Bot routine closed!")
    else:
        return


@client.event
async def tasks(command, time):
    printimed("Command {} will be implemented in {} seconds".format(command, time))
    await asyncio.sleep(time)
    uk.send_command(command)
    printimed("Command {} was implemented".format(command))



@client.event
async def analize_msg(msg):
    if re.search('rumor', msg):
        await printimed('Bot detected, captcha needed...')
    elif re.search('remind',msg):
        pass
    elif re.search('den', msg, re.I):
        await ddmc(msg)
    elif re.search('fishing', msg):
        await fishc(msg)
    elif re.search('daily', msg, re.I):
        await dailyc(msg)
    else:
        printimed('Command not registered')


def getime_second(msg):
    aux = re.search('(\d+)*[hours ]+(\d+)*[minutes and]+(\d+) seconds*', msg)
    out = 0
    if aux:
        for i in aux.groups():
            out += out*60 + int(i) if i else 0

        return out
    else:
        return 0


@client.event
async def ddmc(msg):
    printimed('Den Den Mushi scheduled')
    await tasks('rmd ddm', 10)
    await tasks('ddm', getime_second(msg)+2)


@client.event
async def fishc(msg):
    await tasks('rmd fish', 15)
    printimed('Fish scheduled')
    if re.search('fishing', msg):
        await tasks('fish', getime_second(msg)+2)
    else:
        printimed('Fished...')
        await tasks('fish', 3602)


@client.event
async def dailyc(msg):
    await tasks('rmd daily', 20)
    printimed('Daily scheduled')
    if re.search('received', msg):
        await tasks('daily', getime_second(msg)+2)
    else:
        await tasks('daily', 86402)
        printimed('Got daily bonus...')

'''
def repc(msg):
    pass

def btlac(msg):
    pass

def boatec(msg):
    pass

def boatusec(msg):
    pass

def chapc(msg):
    pass

def chapnextc(msg):
    pass

def ptc(msg):
    pass

def votec(msg):
    pass
'''
