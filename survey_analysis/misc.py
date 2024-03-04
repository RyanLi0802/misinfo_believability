import pandas as pd
import numpy as np
import argparse
from matplotlib import pyplot as plt
from transformers import pipeline
from scipy.stats import ttest_ind


parser = argparse.ArgumentParser()
parser.add_argument("--data_file", type=str)
parser.add_argument("--output_file", type=str)
parser.add_argument("--preprocess", action='store_true')
parser.add_argument("--get_sentiment", action='store_true')
parser.add_argument("--sentiment_analysis", action='store_true')
parser.add_argument("--meta_data", action='store_true')
args = parser.parse_args()

if args.preprocess:
    believability_ratings = {
        "Not believable at all": 0,
        "Somewhat not believable": 1,
        "Neutral": 2,
        "Not applicable": 2,
        "Somewhat believable": 3,
        "Very believable": 4
    }

    annotations = pd.read_csv('Tweet_Annotation-0218.csv', sep=',')
    annotations = annotations.dropna(subset=['Q2A'], inplace=False)

    annotations['Q2A'] = annotations['Q2A'].map(believability_ratings)
    annotations['Q2B'] = annotations['Q2B'].map(believability_ratings)
    annotations['Q2C'] = annotations['Q2C'].map(believability_ratings)

    annotations['avg_rating'] = annotations[['Q2A', 'Q2B', 'Q2C']].mean(axis=1, skipna=True)
    annotations['tweet_real_id'] = annotations['tweet_real_id'].astype(str)

    annotations.to_csv('filtered_annotations.csv', index=False)

annotations = pd.read_csv('filtered_annotations.csv', sep=',')

if args.get_sentiment:
    sentiment = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")
    # for idx, _ in annotations.iterrows():
    #     print(sentiment(annotations.loc[idx, 'text']))
    annotations['sentiment'] = annotations['text'].apply(lambda x: sentiment(x)[0]['label'])
    annotations['sentiment_score'] = annotations['text'].apply(lambda x: sentiment(x)[0]['score'])
    annotations.to_csv('filtered_annotations.csv', index=False)


if args.sentiment_analysis:
    # Group the data by sentiment
    grouped_data = annotations.groupby('sentiment')

    # Calculate the mean and standard deviation of avg_rating for each sentiment category
    mean_rating = grouped_data['avg_rating'].mean()
    std_rating = grouped_data['avg_rating'].std()

    # Print the mean and standard deviation for each sentiment category
    print("Mean of avg_rating:")
    print(mean_rating)
    print("\nStandard Deviation of avg_rating:")
    print(std_rating)

    # Perform appropriate statistical tests to calculate p-values
    # You can use t-test or ANOVA depending on the distribution and assumptions of your data
    # Here's an example using t-test for each sentiment category compared to NEU
    neu_ratings = annotations[annotations['sentiment'] == 'NEU']['avg_rating']
    pos_ratings = annotations[annotations['sentiment'] == 'POS']['avg_rating']
    neg_ratings = annotations[annotations['sentiment'] == 'NEG']['avg_rating']

    _, p_value_pos_neu = ttest_ind(pos_ratings, neu_ratings)
    _, p_value_neg_neu = ttest_ind(neg_ratings, neu_ratings)
    _, p_value_pos_neg = ttest_ind(pos_ratings, neg_ratings)

    print("\np-value (POS vs NEU):", p_value_pos_neu)
    print("p-value (NEG vs NEU):", p_value_neg_neu)
    print("p-value (POS vs NEG):", p_value_pos_neg)

if args.meta_data:
    meta_data = ["retweet_count","user_followers_count","reply_count","like_count","quote_count","bookmark_count","impression_count"]
    for field in meta_data:
        
        bin_ranges = np.arange(0, np.log(annotations[field]).max() + 1, 1)
        bin_labels = [f'{i}-{i+1}' for i in range(len(bin_ranges) - 1)]

        annotations['log_field_bin'] = pd.cut(np.log(annotations[field]), bins=bin_ranges, labels=bin_labels)
        grouped_data = annotations.groupby('log_field_bin')['avg_rating']

        mean_rating = grouped_data.mean()
        std_rating = grouped_data.std()

        plt.bar(mean_rating.index, mean_rating, yerr=std_rating)
        plt.xticks(rotation=45)
        # plt.scatter(np.log(annotations[field]), annotations['avg_rating'])
        # or
        # plt.bar(np.log(annotations[field]), annotations['avg_rating'])
        plt.xlabel(f'log({field})')
        plt.ylabel('avg_rating')
        plt.title(f'Distribution of avg_rating by {field}')
        plt.savefig(f'img/{field}_bar.png')
        plt.close()
        
        
        # now plot the scatter plot 
        plt.figure(figsize=(10, 6))
        plt.scatter(np.log(annotations[field]), annotations['avg_rating'])
        plt.xlabel(f'log({field})')
        plt.ylabel('avg_rating')
        plt.title(f'Distribution of avg_rating by {field}')
        plt.savefig(f'img/{field}_scatter.png')
        plt.close()
    