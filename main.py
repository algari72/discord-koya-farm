from client import client
from log import *
import json
import os



def main():
    with open('files/koya.config', 'r') as f:
        s = f.read()
        s = json.loads(s)

    os.system('clear')
    client.uname = s['username']
    client.prefix = s['prefix']
    client.run(s['token'])

if __name__ == '__main__':
    main()
