import pandas as pd
import json
import uuid


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


def count_keywords(positive_keywords, negative_keywords, basic_dataset):
    positive_keyword_count = []
    for keyword in positive_keywords:
        positive_keyword_count.append([keyword, []])

    negative_keyword_count = []
    for keyword in negative_keywords:
        negative_keyword_count.append([keyword, []])

    for entry in basic_dataset:
        # TODO find keywords in reviews and store their uid
        return


if __name__ == "__main__":
    # _positive_keywords, _negative_keywords = prepare_keywords()
    _basic_dataset = prepare_basic_review_dataset()
    # count_keywords(_positive_keywords, _negative_keywords, _basic_dataset)
