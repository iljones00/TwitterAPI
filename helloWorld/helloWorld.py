# from __future__ import absolute_import, print_function

import tweepy
from privateFields import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print(api.me().name)
api.update_status(status='Hello World!!!')