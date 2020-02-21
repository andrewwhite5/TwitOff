import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

# Grab keys and tokens from .env
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', default='Oops')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET', default='Oops')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', default='Oops')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', default='Oops')

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print(type(auth))

client = tweepy.API(auth)
print(type(client))
print(dir(client))

# # Look at public tweets
# print('\n-----------------')
# public_tweets = client.home_timeline()
# for tweet in public_tweets:
#     print(type(tweet), tweet.text)

# Look at Elon Musk's tweets -- show full tweets
print('\n-----------------')
elon_tweets = client.user_timeline('elonmusk', tweet_mode='extended')
for tweet in elon_tweets:
    print(type(tweet), tweet.full_text)
