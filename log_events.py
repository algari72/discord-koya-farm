import time

def printimed(s):
    t = time.strftime('[%d/%m/%Y  %H:%M:%S]',time.localtime())
    print('\33[1m\33[90m'+t+'\33[0m\33[1m',s,end='\33[0m\n')
    save_event(t + ' ' + str(s))

def save_event(event):
    with open('event.log', 'a') as f:
        f.write(event)
        f.write('\n')
