
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

# example query below

tweets = api.search(q=["vercel serverless"], lang="en", count=noOfTweet)

sentiment_list = []
subjectivity_list = []
tweets_list = []

for tweet in tweets:
    tweets_list.append(str(tweet.text))
    sentiment_list.append(TextBlob(str(tweet.text)).sentiment.polarity)
    subjectivity_list.append(TextBlob(str(tweet.text)).sentiment.subjectivity)

frame = {"Tweet": tweets_list, "Sentiment": sentiment_list, "Subjectivity": subjectivity_list}

df = pd.DataFrame(data=frame) # takes an object

print(df)







