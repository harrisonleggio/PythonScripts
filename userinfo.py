# Credit to Tweepy API docs where credit is needed
import tweepy

# Credentials to my throwaway Twitter account
CONSUMER_KEY = 'sFLL9lXR0ZVUU5P7F26g7tds5'
CONSUMER_SECRET = 'oYNS95rzjWoPDXOfGAW1FzsACSaG2iT6pFBZ4rdVTYN25Rz3nl'
ACCESS_KEY = '717037162903040000-rbf0HtqbhnP8howTSXdMlkt02Vp7fk9'
ACCESS_SECRET = 'Sm5EEAuH2pMD3KxxFwfYPAgOs0AhXYloTvUR6aYwfbrmM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Targeted user
user = api.get_user('harrisonleggio')

# Display user's name, follower count, and who they're following (capped at 20) 
# I believe you can increase it from 20 if you used a cursor and called .items(###) after it.
print ('Username: ' + user.screen_name)
print ('Following: ' + str(user.followers_count))
for friend in user.friends():
    print (friend.screen_name)


















