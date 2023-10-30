from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
from pathlib import Path

# Import tweets emotions dataset
abs_path = Path(".").absolute()
df = pd.read_csv(str(abs_path) + os.sep + "data/tweets-emotions.csv")

# Get summation of total sentiment from all tweets, create representational array
anger = df["Angry"].sum()
fear = df["Fear"].sum()
happy = df["Happy"].sum()
sad = df["Sad"].sum()
surprise = df["Surprise"].sum()

data = [anger, fear, happy, sad, surprise]
emotions = ["Anger", "Fear", "Happy", "Sad", "Surprise"]
 
# Create color parameters
colors = ( "black", "red", "orange",
          "blue", "indigo")
 
wp = { "linewidth" : 1, "edgecolor" : "black" } # Wedge properties
 
# Create autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%".format(pct, absolute)
 
# Create plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  labels = emotions,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="white"))
# Add legend
ax.legend(wedges, emotions,
          title ="Emotions",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
plt.setp(autotexts, size = 9, weight ="bold")
ax.set_title("Emotions of Tweets about Netflix")
 
# Show plot representing general tweet sentiment about Netflix
plt.show()
