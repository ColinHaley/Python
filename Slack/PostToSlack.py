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

# Get config information from ../Authentication/Slack.cfg

config = ConfigParser.RawConfigParser()
config.read('../Authentication/Slack.cfg')

__token__ = config.get('LogPoster','token')

# User token from config file to generate 
client = SlackClient(__token__)
__channel__ = '#logging-scripts'
__username__ = 'Colin'
while True:
    __message__ = raw_input()
    client.chat_post_message(__channel__, __message__, username=__username__)

