import pandas as pd
import json
import uuid
import sys
import collections
from itertools import islice


def prepare_keywords():
    dataframe = pd.read_excel("positive_negative_keywords.xlsx").drop(index=0)
    positive_df = dataframe["Positive Sense Word List"].dropna()
    negative_df = dataframe["Negative Sense Word List"].dropna()
    return positive_df.values.tolist(), negative_df.values.tolist()


def rating_to_label(rating):
    rating = int(rating.split('/')[0])
    label = None
    if rating <= 4:
        label = "Negative"
    elif rating <= 6:
        label = "Neutral"
    elif rating <= 10:
        label = "Positive"
    return label


def prepare_basic_review_dataset(store_as_file=True):
    dataset_files = ["../crawler/data.json"]  # Add here all json files that contain movie reviews and their scores
    data = {}
    for dataset_file_name in dataset_files:
        # Will need method extraction for cleanup and implementation of other methods
        # in case of adding data from different websites
        # This handles iMDB data
        with open(dataset_file_name, 'r') as dataset_file:
            for line in dataset_file:
                entry = json.loads(line)
                if entry["rating"] != "None":
                    label = rating_to_label(entry["rating"])
                    data[str(uuid.uuid4())] = {"review": entry["review"], "rating": entry["rating"], "label": label}
    if store_as_file:
        with open("basic_dataset.json", 'w') as basic_dataset_file:
            json.dump(data, basic_dataset_file)
    return data


def count_keywords(positive_keywords, negative_keywords, basic_dataset, store_as_file=True):
    positive_keyword_count = {}
    for keyword in positive_keywords:
        positive_keyword_count[keyword] = []

    negative_keyword_count = {}
    for keyword in negative_keywords:
        negative_keyword_count[keyword] = []

    counter = 0
    size = len(basic_dataset)
    for uid in basic_dataset:
        # Progress counter
        counter += 1
        print("\rKeyword Counting: " + str(int(100*counter/size)) + "%", end='')
        sys.stdout.flush()

        # Functionality
        review_text = basic_dataset[uid]["review"]
        for keyword in positive_keywords:
            if keyword in review_text:
                positive_keyword_count[keyword].append(uid)
        for keyword in negative_keywords:
            if keyword in review_text:
                negative_keyword_count[keyword].append(uid)

    if store_as_file:
        with open("positive_keywords_count.json", 'w') as positive_file:
            json.dump(positive_keyword_count, positive_file)
        with open("negative_keywords_count.json", 'w') as negative_file:
            json.dump(negative_keyword_count, negative_file)
    return positive_keyword_count, negative_keyword_count


def get_top_n_keywords(n=100):
    with open("positive_keywords_count.json", 'r') as positive_file:
        positive_counts = json.load(positive_file)
        positive_counts = collections.OrderedDict(
            sorted(positive_counts.items(), key=lambda x: len(x[1]), reverse=True))
        positive_counts = dict(islice(positive_counts.items(), n))
        with open("top_positive_keywords_count.json", 'w') as top_positive_file:
            json.dump(positive_counts, top_positive_file)

    with open("negative_keywords_count.json", 'r') as negative_file:
        negative_counts = json.load(negative_file)
        negative_counts = collections.OrderedDict(
            sorted(negative_counts.items(), key=lambda x: len(x[1]), reverse=True))
        negative_counts = dict(islice(negative_counts.items(), n))
        with open("top_negative_keywords_count.json", 'w') as top_negative_file:
            json.dump(negative_counts, top_negative_file)


if __name__ == "__main__":
    # _positive_keywords, _negative_keywords = prepare_keywords()
    # _basic_dataset = prepare_basic_review_dataset(store_as_file=False)
    # pos_count, neg_count = count_keywords(_positive_keywords, _negative_keywords, _basic_dataset, False)
    get_top_n_keywords()
