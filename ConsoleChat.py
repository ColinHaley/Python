"""
I find bash scripts to be pretty gross.
This script will replace the nasty direct send commands used right now
with a more elegant script that enables commands, moderator chats, and direct messages.
"""

from subprocess import call
import ConfigParser
import getpass
import argparse

# Module level variables

def sendAllMessage(message):
    messageString = 'tellraw @a [\"\",{\"text\":\"<\"},{\"text\":\"Kazra\",\"color\":\"dark_red\"},{\"text\":\">: \",\"color\":\"none\"},{\"text\":\"{0}\",\"color\":\"none\"}]'.format(message)
    call(["tmux","send","-t",__instance__,messageString,"ENTER"])

def sendModMessage(message):
    messageString = 'tellraw @a[team=Admins] [\"\",{\"text\":\"[\",\"color\":\"light_purple\"},{\"text\":\"ModChat\",\"color\":\"dark_purple\",\"bold\":true},{\"text\":\"] \",\"color\":\"light_purple\",\"bold\":false},{\"text\":\"Kazra\",\"color\":\"dark_purple\"},{\"text\":\" : {0}\",\"color\":\"light_purple\"}]'.format(message)
    call(["tmux","send","-t",__instance__,messageString,"ENTER"])

def sendCommand(command):
    call(["tmux","send","-t",__instance__,command,"ENTER"])

def sendWhisper(player, message):
    messageString = 'tellraw {0} [\"\",{\"text\":\"<\"},{\"text\":\"{1} whispers: {2}\",\"color\":\"grey\",\"italics\":\"true\"}]'.format(player, __username__, message)
    call(["tmux","send","-t",__instance__,messageString,"ENTER"])

def notifyConnect():
    messageString = 'tellraw @a {\"text\":\"{0} has connected to the console\",\"color\":\"yellow\"}'
    call(["tmux","send","-t",__instance__,messageString,"ENTER"])

config = ConfigParser.RawConfigParser()
config.read('Authentication/ConsoleChat.cfg')

__chatpass__    = config.get('ConsoleChat','password')
__username__    = raw_input('Who are you? ')
__instance__	= 'Admin'

parser = argparse.ArgumentParser()
parser.add_argument('--silent',nargs='?',const=1,type=bool,default=0)
args = parser.parse_args()

__validated__ 	= False
while __validated__ == False:
    __enterpass__ = getpass.getpass('Please enter the console chat password: ')
    if __enterpass__ == __chatpass__:
        __validated__ = True


if __name__ == '__main__':
    if not args.silent:
        notifyConnect()
    while True:
        
