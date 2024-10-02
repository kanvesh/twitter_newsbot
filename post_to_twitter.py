import tweepy

from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.getenv('twitter_consumer_key')
consumer_secret = os.getenv('twitter_consumer_secret')
access_token = os.getenv('twitter_access_token')
access_token_secret = os.getenv('twitter_access_token_secret')

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

def post_tweet(content):
    response = client.create_tweet(text=content)
    print(f"https://twitter.com/user/status/{response.data['id']}")
