import numpy as np
import pandas as pd


few = pd.read_csv('believable_by_few.csv', sep=',')
many = pd.read_csv('believable_by_many.csv', sep=',')

helpful = pd.read_csv('scoredHelpfulNotes.tsv', sep='\t')
helpful_tweets = helpful["tweetId"].drop_duplicates()
print(len(helpful_tweets))
many = many[many["tweetId"].isin(helpful_tweets)]
print(len(many))

many = many.groupby("topic2").sample(n=50, random_state=1)
print(many['topic2'].value_counts())

data = pd.concat([few, many])
print(data.head())
print(data.tail())
data.to_csv("survey_data.csv", sep=',', index=False, header=True)