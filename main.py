from log_events import *
from client import client
from user.keytool import send_command
import os

token = 'NzIxMjM5Mjg2MDkwOTU2ODcx.XuRosg.iEVZuDG7wGSQDj_EBsghtVYIEdU'

def main():
    os.system('clear')
    client.run(token)

if __name__ == '__main__':
    main()
