import numpy as np
import pandas as pd
import json



few = pd.read_csv('believable_by_few.csv', sep=',')
many = pd.read_csv('believable_by_many.csv', sep=',')

print("before merge:")
print(few.shape)
print(many.shape)

few_image = pd.read_csv('believable_by_few_with_imgcap.csv', sep=',')[["tweetId", "media/0/imageDescription", "media/1/imageDescription", "media/2/imageDescription", "media/3/imageDescription"]]
many_image = pd.read_csv('believable_by_many_with_imgcap.csv', sep=',')[["tweetId", "media/0/imageDescription", "media/1/imageDescription", "media/2/imageDescription", "media/3/imageDescription"]]

few = few.merge(few_image, on="tweetId", how="inner")
many = many.merge(many_image, on="tweetId", how="inner")

for df in [few, many]:
    for idx, row in df.iterrows():
        for col in ["media/0/imageDescription", "media/1/imageDescription", "media/2/imageDescription", "media/3/imageDescription"]:
            if not pd.isna(df.at[idx, col]):
                description = df.at[idx, col].replace("image description: {", "").replace("}", "")
                description = description[0].lower() + description[1:]
                df.at[idx, col] = description
                

print("after merge:")
print(few.head())
print(few.shape)
print(many.head())
print(many.shape)

print(few.iloc[8]['media/0/imageDescription'])


few.to_csv("believable_by_few.csv", sep=',', index=False, header=True)
many.to_csv("believable_by_many.csv", sep=',', index=False, header=True)