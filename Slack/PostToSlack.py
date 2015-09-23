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
try:
    import pyslack
except:
    # handle python 3 silly imports
    from pyslack import pyslack

# ConfigParser is a native module, no try except needed
import ConfigParser

# Get config information from ../Authentication/Slack.cfg

config = ConfigParser.RawConfigParser()
config.read('../Authentication/Slack.cfg')
