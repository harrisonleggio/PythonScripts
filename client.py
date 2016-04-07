#********** CREDIT TO GITHUB.COM/LESP FOR HOW I DISPLAYED TWEETS ONE BY ONE AND HANDLED HOME WINDOW BEHAVIOR ********** 

from easygui import *
import sys
import tweepy


CONSUMER_KEY = 'sFLL9lXR0ZVUU5P7F26g7tds5'
CONSUMER_SECRET = 'oYNS95rzjWoPDXOfGAW1FzsACSaG2iT6pFBZ4rdVTYN25Rz3nl'
ACCESS_KEY = '717037162903040000-rbf0HtqbhnP8howTSXdMlkt02Vp7fk9'
ACCESS_SECRET = 'Sm5EEAuH2pMD3KxxFwfYPAgOs0AhXYloTvUR6aYwfbrmM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

msg = "What would you like to do?"
title = "Lite Twitter Client"
choices = ["Follow Back", "Search For Someone","Tweet", "Read Timeline"]

def readTimeline():
    tweets = api.home_timeline()
    for tweet in tweets:
            try:
                tweets = buttonbox(title="Twitter Feed", msg = tweet.text, choices = ("Next", "Exit"))
                if tweets !=  "Next":
                    break
            except:
                sys.exit()
 
def tweet():
    new_tweet = enterbox(msg = "What would you like to tweet?", title="Post Tweet")
    if len(new_tweet) > 140:
        msgbox("Too Long!")
        tweet()
    else:
        api.update_status(new_tweet)
    
def user():
    twitteruser = enterbox(msg = "Who would you like to search for?", title = "Search")
    tweets = api.user_timeline(twitteruser)
    for tweet in tweets:
        try:
            tweets = buttonbox(title=twitteruser + "'s Tweets", msg = tweet.text, choices = ("Next", "Exit"))
            if tweets != "Next":
                break
        except:
            sys.exit()

def followBack():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        msgbox(title="Follow Back", msg="Followed all of your recents followers!")
        
while True:
    choice = choicebox(msg, title, choices)
    if choice == "Search For Someone":
        user()
    elif choice == "Tweet":
        tweet()
    elif choice == "Read Timeline":
        readTimeline()
    elif choice == "Follow Back":
        followBack()
    else:
        sys.exit()



      

