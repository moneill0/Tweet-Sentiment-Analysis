import tweepy
import pandas as pd
from langdetect import detect
import os
from pathlib import Path

# Initialize Twitter developer credentials
client = tweepy.Client(bearer_token= "<your-bearer-token>")
username = "<your-twitter-username"

query = "Netflix" # Word/phrase you want to be included in scraped tweets
tweets = [] # Array to hold scraped tweets
count = 150 # Number of tweets to scrape

# Preprocessing
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,tweet_fields=[], max_results=100).flatten(limit=2000):
    # Only include tweets with more than 3 words
    text = str(tweet)
    word_list = text.split() 
    num_words = len(word_list)
    
    # Only include English tweets
    try:
        language = detect(text)
    except:
        language = "error"
    
    if (language == "en") & (num_words > 3):
        tweets.append(text)
                
# Create dataframe and send to CSV file
df = pd.DataFrame()
df["Tweets"] = tweets   
abs_path = Path(".").absolute()
df.to_csv((str(abs_path) + os.sep + "data/tweets.csv"), index=False)
