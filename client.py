from log import *
from random import random
import keytool as kt
import asyncio
import discord
import time as t
import re

client = discord.Client()

client.cmmd = ''
client.tasked = {
    'ddm': False,
    'fish': False,
    'daily': False
}
client.timed = {
    'ddm': -1,
    'fish': -1,
    'daily': -1
}


@client.event
async def on_ready():
    printimed(f"Client: Bot routine started succesfully as {client.user}.")
    printimed(f"User: User set name as {client.uname}.")


@client.event
async def on_message(msg):

    if msg.author.__str__() == client.uname:
        if msg.content.startswith('/'):
            await command_user(msg)
            pass
        elif msg.content.startswith('koya'):
            pass

        else:
            pass

    elif msg.author.__str__() == "Koya#1050":
        save_msg(msg, client.cmmd)
        await analize_msg(msg.content, client.cmmd)
    else:
        pass


async def command_user(msg):
    cmmd = msg.content
    cmmd = cmmd[1:]

    if cmmd == 'stop':
        await msg.channel.send('Client: Bot routine is closing...')
        await client.close()
        printimed("Client: Bot routine closed.")

    elif cmmd == 'map':
        await send_cmmd('ddm')
        await asyncio.sleep(5)
        await send_cmmd('fish')
        await asyncio.sleep(5)
        await send_cmmd('daily')

    elif cmmd == 'time':
        s = ''
        for i in client.timed:
            s += "{}: {} seconds\n".format(i, int(client.timed[i]-t.time()))
        await msg.channel.send(s)

    elif cmmd == 'free':
        client.cmmd = ''
        client.tasked = {
            'ddm': False,
            'fish': False,
            'daily': False
        }
        client.timed = {
            'ddm': -1,
            'fish': -1,
            'daily': -1
        }
    elif cmmd == 'isactive':
        await msg.channel.send('Still active...')

    else:
        pass


async def send_cmmd(cmmd):
    def check(x):
        return x.author.__str__() == "Koya#1050"

    kt.send_command(cmmd)
    await client.wait_for('message', check=check)
    client.cmmd = cmmd
    printimed("User: command \"{}\" was sent and confirmed.".format(cmmd))


async def tasks(cmmd, time):

    if not client.tasked[cmmd]:
        time = int(time)
        printimed("User: command \"{}\" will be implemented in {} seconds.".format(cmmd, time))
        client.tasked[cmmd] = True
        client.timed[cmmd] = t.time() + time
        await asyncio.sleep(time)
        client.tasked[cmmd] = False
        await send_cmmd(cmmd)


async def analize_msg(msg, cmmd):

    if re.search('/captcha', msg):
        def check(x):
            return x.author.__str__() == client.uname and msg.content.startswith('/free')

        client.tasked = {
            'ddm': True,
            'fish': True,
            'daily': True
        }

        printimed("User: Captcha needed")
        await client.wait_for('message', check=check)


    elif re.search('rmd',cmmd):
        pass
    else:
        func = {
            'ddm': ddmc,
            'fish': fishc,
            'daily': dailyc
        }

        await func[cmmd](msg)


async def ddmc(msg):
    await send_cmmd('rmd ddm')
    t = getime_second(msg)
    await tasks('ddm', t+5*random())


async def fishc(msg):
    await send_cmmd('rmd fish')
    t = getime_second(msg)
    if t == -1:
        await tasks('fish', 3600+10*random())
    else:
        await tasks('fish', t+10*random())


async def dailyc(msg):
    await send_cmmd('rmd daily')
    t = getime_second(msg)
    if t == -1:
        await tasks('daily', 86400+10*random())
    else:
        await tasks('daily', t+10*random())


def getime_second(msg):

    aux = re.search('(\d+)*[hours ]+(\d+)*[minutes and]+(\d+) seconds*', msg)
    out = 0
    if aux:
        for i in aux.groups():
            out += out*60 + int(i) if i else 0
        return out
    else:
        return -1
