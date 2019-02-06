# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:22:04 2019

@author: User
"""

import tweepy
import json
access_token = "157565505-iExQdIo4tsn3qqDpJNiwXA09qEE5gaEa5nHFh2eE"
access_token_secret = "eszpAoirdubjbpymVQcE3sP3S33i4suin7TsWg1nCTcFQ"
consumer_key = "WsTKDIprJzw89JMLLxWfJqVzL"
consumer_secret = "kvSdrqn2Urb3guXdmQiyBqjgA73LQzj99IXGBxC7B3T85CRac5"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweet_list=[]

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")
    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        tweet_list.append(status)
        self.num_tweets += 1
        if self.num_tweets < 1000:
            return True
        else:
            return False
        self.file.close()

# Create Streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)
# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['superbowl','trump','sanders','cruz'])

# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path= 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data=[]

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]


import re

# we have defined the following function word_in_text(), 
#which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet).

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['superbowl', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd,[clinton,trump,sanders, cruz])
ax.set(ylabel="count")
plt.show()

import os
os.path.abspath("tweets.txt")
