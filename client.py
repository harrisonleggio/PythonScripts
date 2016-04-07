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
choices = ["Search For Someone","Tweet", "Read Timeline"]

def readTimeline():
    tweets = api.home_timeline()
    msgbox(
            tweets[0].text + "\n\n" + tweets[1].text + "\n\n" + tweets[2].text +
           "\n\n" + tweets[3].text + "\n\n" +tweets[4].text + "\n\n" +tweets[5].text +
           "\n\n" + tweets[6].text + "\n\n" + tweets[7].text + "\n\n" + tweets[8].text +
            "\n\n" + tweets[9].text + "\n\n" + tweets[10].text + "\n\n" + tweets[11].text
            + "\n\n" + tweets[12].text + "\n\n" + tweets[13].text + "\n\n" + tweets[14].text
            + "\n\n" + tweets[15].text + "\n\n" + tweets[16].text + "\n\n" + tweets[17].text
           + "\n\n" + tweets[18].text + "\n\n" + tweets[19].text)

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
    msgbox(
            tweets[0].text + "\n\n" + tweets[1].text + "\n\n" + tweets[2].text +
           "\n\n" + tweets[3].text + "\n\n" +tweets[4].text + "\n\n" +tweets[5].text +
           "\n\n" + tweets[6].text + "\n\n" + tweets[7].text + "\n\n" + tweets[8].text +
            "\n\n" + tweets[9].text + "\n\n" + tweets[10].text + "\n\n" + tweets[11].text
            + "\n\n" + tweets[12].text + "\n\n" + tweets[13].text + "\n\n" + tweets[14].text
            + "\n\n" + tweets[15].text + "\n\n" + tweets[16].text + "\n\n" + tweets[17].text
           + "\n\n" + tweets[18].text + "\n\n" + tweets[19].text)

while True:
    choice = choicebox(msg, title, choices)
    if choice == "Search For Someone":
        user()
    elif choice == "Tweet":
        tweet()
    elif choice == "Read Timeline":
        readTimeline()
    else:
        sys.exit()



      

