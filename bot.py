import tweepy
from NoUwuBot.secrets import *
from random import randint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    #quotes one in thirty tweets containing "uwu" with the message "NO"
    def on_status(self, status):
        randominteger = randint(0,30)
        if not status.is_quote_status and randominteger == 10:
            api.update_status('NO https://twitter.com/' + status.user.id_str + '/status/' + status.id_str)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#filters the tweet stream with the string "uwu"
myStream.filter(track=['uwu'])

