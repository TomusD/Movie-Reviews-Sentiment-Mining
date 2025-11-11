# Movie Sentiment Analysis Pipeline

A system for large-scale sentiment analysis of movie reviews, featuring a parallel web crawling architecture and multiple machine learning model implementations.

## Architecture

This project is divided into two main components: a parallel web crawler for data acquisition and a machine learning pipeline for sentiment classification.

### 1. Parallel Web Crawler

Handles data scraping from IMDb and TMDB.

* **Technology:** Uses **Selenium** to control browser instances, enabling it to bypass dynamic AJAX pagination (i.e., "Load More" buttons) and mimic user behavior to reduce IP bans.
* **Parallelism:** Employs Python's `multiprocessing` module to run multiple bots concurrently (4 bots total targeting IMDb and TMDB).
* **Concurrency Control:** Implements `FileLock` to ensure safe, atomic writes to output JSON files from parallel processes.

### 2. ML & NLP Pipeline

Processes the raw scraped data and trains classification models.

* **Data Cleaning:** Raw data (~60k reviews) is filtered to remove entries without ratings, resulting in a 50k-review dataset.
* **Label Generation:** Numerical ratings are normalized to a 0-10 scale and mapped to three sentiment labels:
    * **Negative:** [0-4]
    * **Neutral:** (4-6]
    * **Positive:** (6-10]
* **Text Preprocessing:** Standard NLP techniques are applied: convert to lowercase, remove special characters/numbers, remove stopwords, and perform lemmatization.
* **Vectorization:** A **Hashing Vectorizer** converts processed text into numerical features for the models.

---

## Model Performance

Three models were trained using the processed text data. A second experiment using keyword-count features was also conducted.

Here's a technical overview of the machine learning models and methodologies used in the project.

---

## Machine Learning & NLP Pipeline

### Data Processing & Feature Engineering
Before training, the raw review text underwent several processing steps:
* **Label Generation:** Numerical ratings were converted into categorical sentiment labels: **Negative**, **Neutral**, or **Positive**.
* **Text Preprocessing:** Standard NLP cleanup techniques were applied, including converting text to lowercase, removing special characters and numbers, removing stopwords, and performing lemmatization.
* **Vectorization:** A Hashing Vectorizer was used to convert the processed text into numerical features suitable for machine learning.

### Models and Experiments
Three distinct machine learning algorithms were trained and evaluated:
* **Logistic Regression**
* **Support Vector Machine**
* **Naive Bayes**

Two main experiments were conducted with these models:
1.  **Basic Data (Text-Only):** Models were trained using only the pre-processed, vectorized review text as features.
2.  **Experimental Data (Keyword Features):** Models were trained on an augmented dataset that included the text features *plus* secondary features based on positive and negative keyword counts.

## Dataset Characteristics

* **Label Distribution:** The final dataset is imbalanced, with a majority of "Positive" reviews.
* **Token Frequency:** Top tokens include "movie," "film," "character," "good," and "great."
* **Review Length:** Most reviews are short, following a right-skewed distribution.
