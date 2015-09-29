"""
I find bash scripts to be pretty gross.
This script will replace the nasty direct send commands used right now
with a more elegant script that enables commands, moderator chats, and direct messages.
"""

try:
    import subprocess
except:
    from subprocess import subprocess

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

__validated__ 	= False
while __validated__ == False:
    __enterpass__	= getpass.getpass('Please enter the console chat password: ')
    if __enterpass__ == __chatpass__:
        __validated__ = True
