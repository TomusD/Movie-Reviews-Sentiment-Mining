import pandas as pd
import ijson
import json


def prepare_keywords():
    dataframe = pd.read_excel("positive_negative_keywords.xlsx").drop(index=0)
    positive_df = dataframe["Positive Sense Word List"].dropna()
    negative_df = dataframe["Negative Sense Word List"].dropna()
    return positive_df, negative_df


def rating_to_label(rating):
    rating = int(rating.split('/')[0])
    label = None
    if rating <= 2:
        label = "Very Negative"
    elif rating <= 4:
        label = "Negative"
    elif rating <= 6:
        label = "Neutral"
    elif rating <= 8:
        label = "Positive"
    elif rating <= 10:
        label = "Very Positive"
    return label


def prepare_basic_review_dataset():
    dataset_files = ["../crawler/data.json"]  # Add here all json files that contain movie reviews and their scores
    data = []
    for dataset_file_name in dataset_files:
        with open(dataset_file_name, 'r') as dataset_file:
            for line in dataset_file:
                entry = json.loads(line)
                if entry["rating"] != "None":
                    label = rating_to_label(entry["rating"])
                    data.append([entry["review"], entry["rating"], label])
        data = pd.DataFrame(data).dropna()
    return data


if __name__ == "__main__":
    positive_keywords_df, negative_keywords_df = prepare_keywords()
    prepare_basic_review_dataset()
