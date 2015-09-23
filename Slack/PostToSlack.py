"""
__author__ 	= 'Colin Haley'
__purpose__ 	= 'Demo slack to team at work'

##############
#REQUIREMENTS#
##############

* pyslack
	pip install pyslack-real
* ConfigParser
* python 2.7.3 and above

"""
from pyslack import SlackClient
import ConfigParser
import time

# Get config information from ../Authentication/Slack.cfg

config = ConfigParser.RawConfigParser()
config.read('../Authentication/Slack.cfg')

__token__ = config.get('LogPoster','token')

# User token from config file to generate 
client = SlackClient(__token__)
__channel__ = '#logging-scripts'
__username__ = 'Script Logger'

client.chat_post_message(__channel__, 'Update-ComputerStatistics; Start time: 2:03', username=__username__)
time.sleep(2.5)
client.chat_post_message(__channel__, 'Update-ComputerStatistics; End time: 2:05', username=__username__)
__username__ = 'SQL Job Logger'
time.sleep(2.5)
client.chat_post_message(__channel__, 'Repopulate CMDB Table; Start time: 2:05', username=__username__)
time.sleep(2.5)
client.chat_post_message(__channel__, 'Repopulate CMDB Table; End time: 2:05', username=__username__)

raw_input()
__channel__ = '#logging-serverstats'
__username__ = 'Statistics Logger'
client.chat_post_message(__channel__, 'APPSERVER01: [CPU]:20% - [RAM]:64% - [Tasks Running]:2', username=__username__)
time.sleep(1)
client.chat_post_message(__channel__, 'SQLSERVER01: [CPU]:4% - [RAM]:15% - [Open Connections]:12', username=__username__)

raw_input()
__channel__ = '#logging-scripts'


__username__ = 'Raw Input'
while True:
    __message__ = raw_input('What do you want to post to {0} as {1}? '.format(__channel__,__username__))
    if not __message__ == '':
        if '!newname' in __message__:
            __username__ = __message__.split(' ',1)[1]
        else:
            client.chat_post_message(__channel__, __message__, username=__username__)
