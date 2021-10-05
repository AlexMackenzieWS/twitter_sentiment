
# Import libs

import dotenv
import sys
import os
import tweepy
import nltk
# nltk.download('punkt')
from textblob import TextBlob
import pandas as pd

dotenv.load_dotenv()

# pulling env variables from local file

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

noOfTweet = 20

tweets = api.search(q=["vercel"], lang="en", count=noOfTweet)

test_list = []
tweets_list = []

for tweet in tweets:
    tweets_list.append(str(tweet.text))
    test_list.append(TextBlob(str(tweet.text)).sentiment)

# print(test_list)

frame = {"Tweet": tweets_list, "Sentiment": test_list}

df = pd.DataFrame(data=frame) # takes an object

print(df)


# words = "Hello there! how are ya"

# test = TextBlob(words)

# print(test.tags)




