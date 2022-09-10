import tweepy
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#the number of tweets and retweets you want to delete
amt = 300
twitter_handle = 'enter your twitter handle'
tweets = api.user_timeline(screen_name = twitter_handle, count = amt, include_rts = True, 
                            tweet_mode = 'extended')
for tweet in tweets:
    api.destroy_status(tweet.id)
    print("removed")