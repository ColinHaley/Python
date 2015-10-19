"""
Author: Colin Haley, aka Kazra, aka /u/Gemjump
Prerequisites:
	* praw: https://praw.readthedocs.org/en/v3.1.0/
	* MySQLdb: http://mysql-python.sourceforge.net/

Written for Python 2.7.2

Enjoy!
"""

#Check Prerequisites - first three should never fail.
import imp
import random
from random import randint

try:
	if(!imp.find_module('praw')):
		import praw
except ImportError:
	raise ValueError("Unable to import praw. Please install via 'pip install praw'.")

try:
	if(!imp.find_module('MySQLdb')):
		import MySQLdb
except ImportError:
	raise ValueError("Unable to import MySQLdb. Please install via 'apt-get install python-mysqldb'.")


# Static values for reddit connection information.
__reddituser__ = 'reddit_username'
__redditpswd__ = 'reddit_password'
__subreddit__ = 'asov'
__useragentstring__ = 'Descriptive Useragent String for Reddit'

# More statics for SQL connection.
__sqlserver__ = 'sql server address'
__sqluser__ = 'sql username'
__sqlpswd__ = 'sql user password'
__sqldatabase__ = 'sql database name'


# This is where the magic happens.

# This SQL Query should return a single result in format:
# ('BUILDTOPIC')
# SQL Syntax should follow this example query:
# "SELECT COLUMN_NAME FROM TABLE_NAME WHERE [bool]USED = 0 LIMIT 1"
sqlquery = "SELECT BuildTopic FROM BuildContestTopics WHERE Used = 0 LIMIT 1"

# Connect to the database.
db = MySQLdb.connect(__sqlserver__,__sqluser__,__sqlpswd__,__sqldatabase__)

# Select one result and store the return value in var contestItem.
cursor = db.cursor()
result = cursor.execute(sql)
contestItem = cursor.fetchone()[0]

# This sets the bool flag in the database so that the already used topic can't be reused.
updateString = "UPDATE BuildContestTopics Set Used = 1 Where BuildTopic = '" + contestItem + "'"
try:
    cursor.execute(updateString)
    db.commit()
except:
    db.rollback()

db.close()

# At this point we have our build topic, so let's get our prizes.

# Rainstoppers are a custom item we have created on A Scoop Of Vanilla to allow players to control
# the weather via some SelectedItem commandblocks. <link to commands coming soon>
numDiamonds = randint(2,4)
numRainstoppers = randint(3,9)

# The array prizeSelectSet should contain custom prizes you plan on providing.
# Var topPrize contains one random item from that array.
prizeSelectSet = ["Builder\'s Box! (A set of maxed diamond tools)"]
topPrize = prizeSelectSet[randint(0,len(prizeSelectSet)-1)]

# These two are straight forward, pick out your number of diamonds and rainstoppers.
diaPrize = '{0} Diamonds'.format(numDiamonds)
rainstopperPrize = '{0} Rain Stoppers'.format(numRainstoppers)

# This is all customized to our server, A Scoop Of Vanilla - just formatting and configuring the text body of a reddit post using Markup. 
# Change them as needed.
prizeString = 'This weeks prize for first place is:\n\n* {0}\n\nAll participants will receive:\n\n* {1}\n* {2}'.format(topPrize, diaPrize, rainstopperPrize)
linkTopic = '[{0}](https://en.wikipedia.org/wiki/{0})'.format(contestItem)
postTitle = 'Bi-Weekly Build Contest: {0}'.format(contestItem)
postBody = 'Hey Scoopers,\n\nThis weeks bi-weekly build contest topic is:\n\n **{0}** \n\n --- \n\nThe rules are simple!\n\n1. Build whatever you can dream based on the theme.\n2. Submit it here!\n3. After 2 weeks, the most upvoted picture wins!\n\n---\n\n{1}'.format(linkTopic, prizeString)

# Connect to Reddit using PRAW and post. No error handling here as of now since PRAW handles most hard exceptions. This might change in the future.
r = praw.Reddit(__useragentstring__)
r.login(__reddituser__,__redditpswd__)
r.submit(__SUBREDDIT__,postTitle,text=postBody)
