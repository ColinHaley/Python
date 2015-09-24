"""
__author__	= 'Colin Haley, aka /u/Gemjump'
__purpose__ 	= 'Watch a list of subreddits for a different list of keywords'

# Other Resources


# Mandatory External Libraries
Praw:		https://gist.github.com/shrayasr/100005943

"""

try:
    import praw
except:
    # Python 3 handling
    from praw import praw

r = praw.Reddit('Searcher for things I care about on Reddit; Made my /u/Gemjump; Run on Debian Wheezy')

listOfSubreddits = ['frugalmalefashion']
listOfKeyWords = ['Wolverine','REI']

for x in range(0,len(listOfSubreddits)):
    
    sub = r.get_subreddit(listOfSubreddits[x],fetch=True)

    posts = sub.get_new()

    while True:
        try:
            time.sleep(2.5)
            post = next(posts)
            for x in range(0,len(listOfKeyWords)):
                if listOfKeyWords[x] in post.title:
                    print post.id
