import pandas as pd
from nltk.util import ngrams

def by_search_term(search_term, tweets):
    """
    Filters list of tweets by looking for a certain term (search_term). The function only returns (cleaned) tweets that contain the search_term.
    The tweets are returned as a pandas dataframe.
    """
    filtered_data = []
    for index, tweet in tweets.iterrows():
        for sentence_words in tweet['sentences']:
            if search_term in sentence_words:
                filtered_data.append(tweet)
    return pd.DataFrame(data=filtered_data)

def by_hashtag(hashtag, tweets):
    """
    Filters list of tweets by looking for a certain hashtag. The function only returns (cleaned) tweets that contain the hashtag.
    The tweets are returned as a pandas dataframe.
    """
    filtered_data = []
    for index, tweet in tweets.iterrows():
        if tweet['entities.hashtags'] != None and hashtag in get_hashtags(tweet['entities.hashtags']):
            filtered_data.append(tweet)
    return pd.DataFrame(data=filtered_data)

def get_hashtags(hashtag_entitites):
    """Returns a list of lowercase hashtags from the dictionary of hashtag entities return by Twitter's API."""
    return [e['tag'].lower() for e in hashtag_entitites]

def by_ngram(ngram, tweets):
    """
    Filters list of tweets by looking for a certain ngram. The function only returns (cleaned) tweets that contain the ngram.
    The tweets are returned as a pandas dataframe.
    """
    filtered_data = []
    for index, tweet in tweets.iterrows():
        for sentence_words in tweet['sentences']:
            ngram_list = list(ngrams(sentence_words, len(ngram)))
            if ngram in ngram_list:
                filtered_data.append(tweet)
    return pd.DataFrame(data=filtered_data)