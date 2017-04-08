"""
Author: Colin Haley, aka Kazra, aka /u/Gemjump
Prerequisites:
	* praw: https://praw.readthedocs.org/en/v3.1.0/
	* MySQLdb: http://mysql-python.sourceforge.net/

Written for Python 2.7.2

Enjoy!
"""

import urllib2

__useragentstring__ = 'A poster for recruitment threads for /r/asov, written by /u/Gempjump'
__reddituser__ = 'ASOV_Server'
__redditpswd__ = ''
__SUBREDDIT__ = 'mcservers'

try:
	if(!imp.find_module('praw')):
		import praw
except ImportError:
	raise ValueError("Unable to import praw. Please install via 'pip install praw'.")

postUrl = "https://raw.githubusercontent.com/ColinHaley/AScoopOfVanilla/master/Resources/RecruitmentPost.md"

response = urllib2.urlopen(postUrl
postBody = response.read()

postTitle = 'A Scoop of Vanilla [SMP][Semi-Vanilla]{Whitelist}{1.11.2}'

# Connect to Reddit using PRAW and post. No error handling here as of now since PRAW handles most hard exceptions. This might change in the future.
r = praw.Reddit(__useragentstring__)
r.login(__reddituser__,__redditpswd__)
r.submit(__SUBREDDIT__,postTitle,text=postBody)
