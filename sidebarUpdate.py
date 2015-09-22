"""
__author__	= 'Colin Haley, aka Kazra'
__purpose__ 	= 'Update the /r/asov sidebar with online players from asov Vanilla'

Steps:
    1. Create upload variables: [string]CSS, [string]Sidebar
    2. Get current players
        a. If 0:
            i. Clear Sidebar Playerheads
            ii. Set to "No Players Online."
            ii. Exit()
        b. If >= 1:
            i. For each player online:
                - If their img exists in /data && newer than GETDATE()-3:
                    1. Add Strings to CSS and Sidebar variables.
                - If not:
                    1. If older than GETDATE()-7, delete old playerhead icon.
                    2. wget or python equivalent to ~/srv/_config/data/ their player head icon
                    3. rename from 32.png to playername.png
                    4. Upload image
                - Update Users table with:
                    1. UPDATE Users set Timestamp = NOW() WHERE Username = 'playername'

# Other Resources
http://cravatar.us/head/__playername__/32.png
    Even unclaimed names return a 'Steve' head, no error handling needed? Dangerzone

https://www.reddit.com/dev/api
    #POST_api_upload_sr_img
    #POST_api_delete_sr_img

https://github.com/reddit/reddit/wiki/OAuth2

# Mandatory External Libraries
Praw:		https://gist.github.com/shrayasr/100005943
Mcstatus:	https://github.com/Dinnerbone/mcstatus

"""

# Imports
import praw
import time
import datetime
from mcstatus import MinecraftServer
import urllib

#Static Variables

__clientID__ = 'redditClientID'
__secretkey__ = 'redditSecretKey'
__subreddit__ = 'subredditName'
__username__ = 'redditUsername'
__password__ = 'redditPassword'
__serveraddress__ = 'minecraftAddress'
__serverport__ = #RCON Port for Minecraft
__datadirectory__ = '/dir/to/location/to/store/playerheads'

# Section to display playerheads within on the sidebar on reddit.
__sidebarheader__	= '[](/STARTONLINEPLAYERS)'
__sidebarfooter__	= '[](/ENDONLINEPLAYERS)'

# Header for CSS to update playerheads online.
__cssheader__		= '/* END ONLINE PLAYER HEADS DO NOT DELETE OR MOVE FROM HEADER POSITION */'

def generate_css(playerName):
    # return a string formatted "a[href="/playername"]:after { content: url(%%playername%%) }"
    # change this to a .format(playername) at some later point.
    return 'a[href="/' + playerName + ']:after { content: url(%%'+ playerName + '%%) }'

def generate_sidebar(playerName):
    # return a string formatted "[](/playername)"
    # change this to a .format(playerName) at some point.
    return '[](/' + playerName + ')'

def clear_sidebar():
    # Needs to iterate through players currently listed online and remove their image uploads.
    # Requires open connection to Reddit through use of global 'r' variable.
    sidebar = r.get_settings(__subreddit__)['Description']

    clearString = sidebar[:sidebar.index(__sidebarheader__) + len(__sidebarheader__) + sidebar[sidebar.index(__sidebarfooter__):]

    r.update_settings(r.get_subreddit(__subreddit__), description = clearString)

def get_css():
    stylesheet = r.get_stylesheet(__subreddit__)
    return stylesheet

def clear_css():
    # Delete all CSS between two marker comments, using indexOf("str")
    # Requires open connection to reddit via 'r' global
    subCSS = get_css()
    r.set_stylesheet(__subreddit__, [__header__:])


def upload_css_to_reddit(stringCSS):
    # takes .join() list of generateCSS(playername) as a string for upload
    r.set_stylesheet(__subreddit__, stringCSS)

def upload_sidebar_to_reddit(stringSidebar):
    # takes .join() list of generateSidebar(playername) as a string for upload

def getCurrentPlayers():
    server = MinecraftServer(__serveraddress__, __serverport__)
    try:
        query = server.query()
        return {'Count': query.players.online, 'Players':query.players.names}
    except:
        exit()
    
def download_playerhead(playername):
    downloadPath = 'http://cravatar.eu/head/' + playername + '/32.png'
    savepath = __datadirectory__ + playername + '.png'
    urllib.urlretrieve(downloadPath, savePath)   
    # grabs a player head from cravatar to the data folder.

def upload_image_to_reddit(playername):
    __imagedir__ = __datadirectory__ + playername + '.png'
    r.upload_image(__subreddit__, __imagedir__, playername)

def delete_image_from_reddit(playername):
    r.delete_image(__subreddit__, name=playername, header=False) 

def parse_players_from_sidebar()

# Get the players online from the server via RCON
# if unsure of the address use MinecraftServer.lookup()
server = MinecraftServer(__serveraddress__, __serverport__)

try:
    query = server.query()
    if query.players.online > 0:
        #do stuff
    else
        #set sidebar to 'No Players Online'
	clear_css()
	clear_sidebar()
except:
    exit()

#Define the Praw useragent

settings = r.get_settings(__subreddit__)
