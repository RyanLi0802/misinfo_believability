import pandas as pd
import numpy as np


def get_test_set():
    believable_by_few = pd.read_csv('../believable_by_few.csv', sep=',')
    believable_by_many = pd.read_csv('../believable_by_many.csv', sep=',')

    liwc_few = pd.read_csv('../believable_by_few_liwc.csv', sep=',')
    liwc_many = pd.read_csv('../believable_by_many_liwc.csv', sep=',')
    # we are dropping emotion as we are obtaining emotion values from elsewhere
    liwc_few = liwc_few.drop(columns='emotion')
    liwc_many = liwc_many.drop(columns='emotion')

    believable_by_few = believable_by_few.merge(
        liwc_few, on="tweetId", how="inner")
    believable_by_many = believable_by_many.merge(
        liwc_many, on="tweetId", how="inner")

    return believable_by_few.iloc[-20:], believable_by_many.iloc[-20:]


def get_train_set():
    believable_by_few = pd.read_csv('../believable_by_few.csv', sep=',')
    believable_by_many = pd.read_csv('../believable_by_many.csv', sep=',')

    liwc_few = pd.read_csv('../believable_by_few_liwc.csv', sep=',')
    liwc_many = pd.read_csv('../believable_by_many_liwc.csv', sep=',')
    # we are dropping emotion as we are obtaining emotion values from elsewhere
    liwc_few = liwc_few.drop(columns='emotion')
    liwc_many = liwc_many.drop(columns='emotion')

    believable_by_few = believable_by_few.merge(
        liwc_few, on="tweetId", how="inner")
    believable_by_many = believable_by_many.merge(
        liwc_many, on="tweetId", how="inner")

    return believable_by_few.iloc[:50], believable_by_many.iloc[:50]


def extract_features(data):
    features = []
    for idx in range(data.shape[0]):
        row = data.iloc[idx]

        # we first process the metadata
        meta_data = np.concatenate(
            (row[2:7].to_numpy(dtype=np.float64), row[8:10].to_numpy(dtype=np.float64)))
        meta_data = np.log(meta_data, where=(meta_data != 0))
        meta_data = np.append(meta_data, row['user_verified'])

        # now sentiment
        sentiment = np.zeros(1)
        if row["sentiment"] == 'Negative':
            sentiment[0] = -1
        elif row["sentiment"] == 'Positive':
            sentiment[0] = 1

        # emotions
        emotions = row[13:20].to_numpy(dtype=np.float64)

        # topic
        topic = np.zeros(1)
        if row["topic"] == 'politics':
            topic[0] = 1
        elif row["topic"] == 'health':
            topic[0] == 2
        elif row['topic'] == 'science':
            topic[0] = 3
        elif row['topic'] == 'crime':
            topic[0] = 4
        elif row['topic'] == 'religion':
            topic[0] = 5

        # toxicity
        toxicity = row[21:28].to_numpy(dtype=np.float64)

        # liwc
        liwc_columns = ['WC', 'WPS', 'they', 'number', 'adverb', 'Drives', 'power', 'cause', 'discrep', 'friend', 'politic', 'leisure',
                        'relig', 'need', 'fatigue', 'allure', 'visual', 'focuspast', 'Conversation', 'AllPunc', 'Comma', 'Exclam', 'OtherP']
        liwc = row[liwc_columns].to_numpy(dtype=np.float64)

        row_features = np.concatenate(
            (meta_data, sentiment, emotions, topic, toxicity, liwc))
        features.append(row_features)
    features = np.array(features)

    return features


def eval_metrics(labels, targets):
    if len(labels) != len(targets):
        raise Exception("labels and targets must have the same length")

    true_pos = true_neg = false_pos = false_neg = 0

    for i, a in enumerate(labels):
        if a == 1 and targets[i] == 1:
            true_pos += 1
        elif a == 0 and targets[i] == 0:
            true_neg += 1
        elif a == 1 and targets[i] == 0:
            false_pos += 1
        else:   # a == 0 and targets[i] == 1
            false_neg += 1

    accuracy = (true_pos + true_neg) / len(labels)
    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / (true_pos + false_neg)
    f1 = 2 * precision * recall / (precision + recall)

    print(f'accuracy: {accuracy}')
    print(f'precision: {precision}')
    print(f'recall: {recall}')
    print(f'f1 score: {f1}')

    return accuracy, precision, recall, f1
