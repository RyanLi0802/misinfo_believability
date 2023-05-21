from matplotlib import pyplot as plt

import argparse
import subprocess
import numpy as np
import pandas as pd
import scipy.stats as stats


def plot_distribution(few_feature, many_feature, feature_name, pval, output_dir='distributions/'):
    df = pd.DataFrame({"many": many_feature, "few": few_feature})
    ax = df.plot.hist(bins=100, alpha=0.5)
    if pval:
        plt.annotate(f"p-value = {pval}",
                     xy=(0.5, 0.5), xycoords='axes fraction')
    plt.gca().set(title=feature_name.replace("_", " "))
    plt.savefig(output_dir + feature_name, dpi=200)
    plt.close()


def process_numerical_feature(few, many, feature, output_dir='distributions/', filter=False):
    print(f"processing {feature}...")
    few_feature = few[feature]
    many_feature = many[feature]

    if filter:
        # filter out any features that doesn't meet the level of significance
        _statistic, pvalue = stats.mannwhitneyu(
            few_feature.to_numpy(), many_feature.to_numpy())
        if pvalue > 0.1:
            print()
            print()
            return

    few_mean = few_feature.mean()
    few_median = few_feature.median()
    few_std = few_feature.std()
    print("believable by few:")
    print("mean, median, std")
    print(few_mean, few_median, few_std)
    print()

    many_mean = many_feature.mean()
    many_median = many_feature.median()
    many_std = many_feature.std()
    print("believable by many:")
    print("mean, median, std")
    print(many_mean, many_median, many_std)

    # _statistic, pvalue = stats.ttest_ind(few_feature.to_numpy(), many_feature.to_numpy(), equal_var=False)
    # _statistic, pvalue = stats.kruskal(few_feature.to_numpy(), many_feature.to_numpy())
    _statistic, pvalue = stats.mannwhitneyu(
        few_feature.to_numpy(), many_feature.to_numpy())
    print(f"pvalue: {pvalue}")
    print()
    print()

    plot_distribution(few_feature, many_feature, feature, pvalue, output_dir)


def process_cat_feature(few, many, feature):
    print("processing " + str(feature) + "...")
    few = few[feature].value_counts()
    many = many[feature].value_counts()
    print("believable by few:")
    print(few)
    print()
    print("believable by many:")
    print(many)

    sent_table = np.stack([many.to_numpy(), few.to_numpy()])
    _statistic, pvalue, _dof, _expected_freq = stats.chi2_contingency(
        sent_table)
    print(f"pvalue: {pvalue}")
    print()
    print()


def process_img_features(few, many):
    numerical_features_list = ['media_count']
    cat_features_list = ['celebrity_presence', 'text_presence']

    for feature in numerical_features_list:
        process_numerical_feature(
            few, many, feature, "distributions/IMG/", False)
    for feature in cat_features_list:
        process_cat_feature(few, many, feature)


if __name__ == "__main__":

    print("processing image features")
    img_few = pd.read_csv(
        './datasets/believable_by_few_img_features.csv', sep=',')
    img_many = pd.read_csv(
        './datasets/believable_by_many_img_features.csv', sep=',')
    img_features = img_many.columns.tolist()[2:]
    process_img_features(img_few, img_many)
