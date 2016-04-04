# CREDIT: TWEEPY API DOCS
import tweepy

# keys for my throwaway twitter account
CONSUMER_KEY = 'sFLL9lXR0ZVUU5P7F26g7tds5'
CONSUMER_SECRET = 'oYNS95rzjWoPDXOfGAW1FzsACSaG2iT6pFBZ4rdVTYN25Rz3nl'
ACCESS_KEY = '717037162903040000-rbf0HtqbhnP8howTSXdMlkt02Vp7fk9'
ACCESS_SECRET = 'Sm5EEAuH2pMD3KxxFwfYPAgOs0AhXYloTvUR6aYwfbrmM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print (follower.screen_name)
