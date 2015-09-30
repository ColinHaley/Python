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

config = ConfigParser.RawConfigParser()
config.read('Authentication/ConsoleChat.cfg')

__chatpass__	= config.get('ConsoleChat','password')
__username__	= raw_input('Who are you? ')

# Validate admin by password confirmation

def sendAllMessage(message):
    preformatString = 'tellraw @a [\"\",{\"text\":\"<\"},{\"text\":\"Kazra\",\"color\":\"dark_red\"},{\"text\":\">: \",\"color\":\"none\"},{\"text\":\"{0}\",\"color\":\"none\"}]'.format(message)
    call(["tmux","send","-t","vanilla",message,"ENTER"])

__validated__ 	= False
while __validated__ == False:
    __enterpass__ = getpass.getpass('Please enter the console chat password: ')
    if __enterpass__ == __chatpass__:
        __validated__ = True

if __name__ == '__main__':
    # Do stuff
