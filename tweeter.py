# CREDIT TO ROBIN CAMILLE DAVIS
import tweepy, time

# taken from www.apps.twitter.com
# throwaway twitter account so I don't care if it's public
CONSUMER_KEY = 'sFLL9lXR0ZVUU5P7F26g7tds5'
CONSUMER_SECRET = 'oYNS95rzjWoPDXOfGAW1FzsACSaG2iT6pFBZ4rdVTYN25Rz3nl'
ACCESS_KEY = '717037162903040000-rbf0HtqbhnP8howTSXdMlkt02Vp7fk9'
ACCESS_SECRET = 'Sm5EEAuH2pMD3KxxFwfYPAgOs0AhXYloTvUR6aYwfbrmM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


filename=open('testtweets.txt','r')
f=filename.readlines()
filename.close()


for line in f:
     api.update_status(line)
     print (line)
     time.sleep(3) 
