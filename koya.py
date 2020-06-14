from log_events import *
import asyncio
import re

#--commands--
#ddm den den mushi
#fish :fishing_pole_and_fish:
#daily daily
#btl a fight
#boat e 'n' :Franky:
#rep 'name' reputation
#boat use
#chap
#chap next
#p -t
#vote



async def tasks(command, time):
    await asyncio.sleep(time)
    printimed(command+'implemented')

def analize_msg(msg):
    if re.search('rumor', msg):
        printimed('Bot detected, captcha needed...')
    elif re.search('den',msg, re.I):
        ddmc(msg)
    elif re.search('<:fishing',msg):
        fishc(msg)
    elif re.search('daily',msg, re.I):
        dailyc(msg)
    else:
        printimed('Command not registered')

    return True

def getime_second(msg):
    aux = re.search('(\d+)*[hours ]+(\d+)*[minutes and]+(\d+) seconds*',msg)
    out = 0

    for i in aux.groups():
        out += out*60 + int(i) if i else 0

    return out


def ddmc(msg):
    tasks('ddm',getime_second(msg)+2)
    tasks('rmd ddm',0)
    printimed('Den Den Mushi scheduled')


def fishc(msg):
    if re.search('fishing', msg):
        task('fish',getime_second(msg)+2)
    else:
        task('fish',3602)
        printimed('Fished...')

    task('rmd fish',0)
    printimed('Fish scheduled')


def dailyc(msg):
    if msg.find(':koyabotConfused:'):
        task('daily',getime_second(msg)+2)
    else:
        task('daily',86402)
        printimed('Got daily bonus...')

    task('rmd daily',0)
    printimed('Daily scheduled')


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
