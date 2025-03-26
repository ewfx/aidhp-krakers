# run_analysis.py
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.sentiment_analysis import analyze_sentiment

print(analyze_sentiment("Mobile app is decent but can be improved"))

""" 
# Load the sample social media posts
posts = pd.read_csv('inputs/large_social_media_sentiments.csv')

# Analyze sentiment for each post
posts['sentiment'] = posts['Content'].apply(analyze_sentiment)

# Save the results to a new CSV
posts.to_csv('inputs/analysed_social_media_sentiments.csv', index=False)

# Optionally, save to a JSON file
#posts.to_json('outputs/results.json', orient='records', lines=True)
 """