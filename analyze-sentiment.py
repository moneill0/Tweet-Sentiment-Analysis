import text2emotion as te
import pandas as pd
import os
from pathlib import Path

# Import tweets dataset
abs_path = Path(".").absolute()
tweets = pd.read_csv(str(abs_path) + os.sep + "data/tweets.csv")

# Initialize arrays to hold scores respresnting the votality of each emotion demonstrated in a tweet
angry = []
fear = []
happy = []
sad = []
surprise = []

# Get scores to represent emotion in each tweet, append score to dataset
for i in range(len(tweets)):
    emotion = te.get_emotion(str(tweets.values[i]))
    angry.append(emotion["Angry"])
    fear.append(emotion["Fear"])
    happy.append(emotion["Happy"])
    sad.append(emotion["Sad"])
    surprise.append(emotion["Surprise"])
    
# Create csv file to hold data 
tweets["Angry"] = angry
tweets["Fear"] = fear
tweets["Happy"] = happy
tweets["Sad"] = sad
tweets["Surprise"] = surprise
tweets.to_csv((str(abs_path) + os.sep + "data/tweets-emotions.csv"), index=False)
