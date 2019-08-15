# from __future__ import absolute_import, print_function

import tweepy
import json
from privateFields import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

'''
basic account method examples

# print(api.me().name)
# api.retweets(1161209048257245184, 5)
# api.create_friendship("realpython")
# api.update_status(status='Hello World!!!')
'''

'''
This is how to get tweets in a timeline

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
'''

'''
This is how to get information from a user

# user = api.get_user("StephenCurry30")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)
'''

'''
How to look for key words
for tweet in api.search(q="Hong Kong", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
'''
'''
This outputs a list of all trends at a certain location (USA)

trends_result = api.trends_place(23424977)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

This outputs a list of the places and information that the api contains    
# trends_result = api.trends_available()
# for trend in trends_result:
#     print(trend)
''' 

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])
stream.filter(track=['python'], is_async=True) #this runs the filer on a different thread