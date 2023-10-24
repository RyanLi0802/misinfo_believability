import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def plot_distribution(features, feature_name, output_dir='distributions/', x_label = "", y_label = ""):
    df = pd.DataFrame({feature_name: features})
    ax = df.plot.hist(bins=200, alpha=0.5)
    if x_label: 
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    # if pval:
    #     plt.annotate(f"p-value = {pval}", xy=(0.5, 0.5), xycoords='axes fraction')
    plt.gca().set(title=feature_name.replace("_", " "))
    plt.savefig(output_dir + feature_name, dpi=200)
    plt.close()

survey_data = pd.read_csv('survey_data_filtered.csv', sep=',')

plot_distribution(np.log10(survey_data["user_followers_count"]), "user_followers_distribution", x_label="log of # followers")

plt.figure(figsize=(15,12))
survey_data["topic2"].value_counts().plot(kind='bar')
plt.xticks(rotation=20, ha='right')
plt.gca().set(title="topics distribution")
plt.savefig('distributions/topics_distribution', dpi=200)
plt.close()

before_2022 = 0
since_2022 = 0
for idx, row in survey_data.iterrows():
    year = int(row['created_at'].split()[-1])
    if year < 2022:
        before_2022 += 1
    else:
        since_2022 += 1

df = pd.DataFrame({"before_2022": before_2022, "since_2022": since_2022}, index=[0])
df.plot(kind="bar")
plt.gca().set(title="tweet creation time")
plt.savefig('distributions/tweet_time_0', dpi=200)
plt.close()

few = pd.read_csv('believable_by_few.csv', sep=',')
many = pd.read_csv('believable_by_many.csv', sep=',')
all_data = pd.concat([few, many], ignore_index=True)




plot_distribution(np.log10(all_data["user_followers_count"]), "user_followers_distribution_all", x_label="log of # followers")

plt.figure(figsize=(15,12))
all_data["topic2"].value_counts().plot(kind='bar')
plt.xticks(rotation=20, ha='right')
plt.gca().set(title="topics distribution")
plt.savefig('distributions/topics_distribution_all', dpi=200)
plt.close()

before_2022 = 0
since_2022 = 0
for idx, row in all_data.iterrows():
    year = int(row['created_at'].split()[-1])
    if year < 2022:
        before_2022 += 1
    else:
        since_2022 += 1

df = pd.DataFrame({"before_2022": before_2022, "since_2022": since_2022}, index=[0])
df.plot(kind="bar")
plt.gca().set(title="tweet creation time")
plt.savefig('distributions/tweet_time_all', dpi=200)
plt.close()

plot_distribution(np.log10(all_data["retweet_count"], where=all_data["retweet_count"] != 0), "retweet_distribution_all", x_label="log of # of retweets")
plot_distribution(np.log10(survey_data["retweet_count"], where=survey_data["retweet_count"] != 0), "retweet_distribution", x_label="log of # of retweets")
plot_distribution(np.log10(all_data["favorite_count"], where=all_data["favorite_count"] != 0), "favorite_distribution_all", x_label="log of # of favorites")
plot_distribution(np.log10(survey_data["favorite_count"], where=survey_data["favorite_count"] != 0), "favorite_distribution", x_label="log of # of favorites")


# survey_data = survey_data[survey_data["valid"] == True]

# print(survey_data.head(15))
# print(survey_data.tail())

# survey_data.to_csv("survey_data_filtered.csv", sep=',', index=False, header=True)