import time

def printimed(s):
    t = time.strftime('[%d/%m/%Y  %H:%M:%S]',time.localtime())

    print('\33[1m\33[90m'+t+'\33[0m\33[1m',s,end='\33[0m\n')

    with open('files/event.log', 'a') as f:
        f.write(t + ' ' + str(s))
        f.write('\n')

def save_msg(msg, cmmd):
    with open('files/msg.log', 'a') as f:
        f.write('_'*80 + '\n\n')
        f.write(cmmd + '\n\n')
        f.write(msg.__str__() + '\n\n')
        f.write(msg.content + '\n\n')
