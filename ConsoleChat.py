"""
I find bash scripts to be pretty gross.
This script will replace the nasty direct send commands used right now
with a more elegant script that enables commands, moderator chats, and direct messages.
"""
from subprocess import call

try:
    import ConfigParser
except:
    from ConfigParser import ConfigParser
try:
    import getpass
except:
    from getpass import getpass

# Module level variables

def sendAllMessage(message):
    messageString = 'tellraw @a [\"\",{\"text\":\"<\"},{\"text\":\"Kazra\",\"color\":\"dark_red\"},{\"text\":\">: \",\"color\":\"none\"},{\"text\":\"{0}\",\"color\":\"none\"}]'.format(message)
    call(["tmux","send","-t","vanilla",messageString,"ENTER"])

def sendModMessage(message):
    messageString = 'tellraw @a[team=Admins] [\"\",{\"text\":\"[\",\"color\":\"light_purple\"},{\"text\":\"ModChat\",\"color\":\"dark_purple\",\"bold\":true},{\"text\":\"] \",\"color\":\"light_purple\",\"bold\":false},{\"text\":\"Kazra\",\"color\":\"dark_purple\"},{\"text\":\" : {0}\",\"color\":\"light_purple\"}]'.format(message)
    call(["tmux","send","-t","vanilla",messageString,"ENTER"])


config = ConfigParser.RawConfigParser()
config.read('Authentication/ConsoleChat.cfg')

__chatpass__    = config.get('ConsoleChat','password')
__username__    = raw_input('Who are you? ')

__validated__ 	= False
while __validated__ == False:
    __enterpass__ = getpass.getpass('Please enter the console chat password: ')
    if __enterpass__ == __chatpass__:
        __validated__ = True

if __name__ == '__main__':
    # Do stuff