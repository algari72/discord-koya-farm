from log import *
import keytool as kt
import asyncio
import discord
import re

client = discord.Client()

client.cmmd = ''


@client.event
async def on_ready():
    printimed(f"Client: Bot routine started succesfully as {client.user}.")
    printimed(f"User: User set name as {client.uname}.")


@client.event
async def on_message(msg):

    if msg.author.__str__() == client.uname:
        if msg.content.startswith('/'):
            await command_user(msg.content)
            pass
        elif msg.content.startswith('koya'):
            pass

        else:
            pass

    elif msg.author.__str__() == "Koya#1050":
        await analize_msg(msg.content, client.cmmd)
    else:
        pass

async def command_user(cmmd):
    cmmd = cmmd[1:]
    if cmmd == 'stop':
        await msg.channel.send('Client: Bot routine is closing...')
        await client.close()
        printimed("Client: Bot routine closed.")
    elif cmmd == 'map':
        await send_cmmd('ddm')
        await send_cmmd('fish')
        await send_cmmd('daily')
        pass
    else:
        pass


@client.event
async def send_cmmd(cmmd):
    def check(x):
        return x.author.__str__() == "Koya#1050"

    kt.send_command(cmmd)
    await client.wait_for('message', check=check)
    client.cmmd = cmmd
    printimed("User: command \"{}\" was sent and confirmed.".format(cmmd))


@client.event
async def tasks(command, time):
    printimed("User: command \"{}\" will be implemented in {} seconds.".format(command, time))
    await asyncio.sleep(time)
    await send_cmmd(command)


@client.event
async def analize_msg(msg, cmmd):
    if re.search('rumor', msg):
        pass
    else:
        func = {
            'ddm': ddmc,
            'fish': fishc,
            'daily': dailyc
        }
        await func[cmmd](msg)


@client.event
async def ddmc(msg):
    t = getime_second(msg)
    await tasks('ddm', t+2)


@client.event
async def fishc(msg):
    t = getime_second(msg)
    if t == -1:
        await tasks('fish', 3602)
    else:
        await tasks('fish', t+2)


@client.event
async def dailyc(msg):
    t = getime_second(msg)
    if t == -1:
        await tasks('daily', 86402)
    else:
        await tasks('daily', t+2)


def getime_second(msg):
    aux = re.search('(\d+)*[hours ]+(\d+)*[minutes and]+(\d+) seconds*', msg)
    out = 0
    if aux:
        for i in aux.groups():
            out += out*60 + int(i) if i else 0
        return out
    else:
        return -1
