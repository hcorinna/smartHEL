from nltk.util import ngrams
from collections import Counter

def filter_ngrams(ngrams_counter, stop_words):
    """Removes stop_words from the collection of ngrams."""
    filtered_ngrams_counter = []
    for ngram in list(ngrams_counter):
        if any(word in stop_words for word in ngram):
            del ngrams_counter[ngram]
    return filtered_ngrams_counter

def get_ngram_counter(tweets, n, stop_words, ngrams_to_remove):
    """Creates a collection.Counter of ngrams."""
    ngrams_list = get_ngrams(tweets, n, ngrams_to_remove)
    ngrams_counter = Counter(ngrams_list)
    filter_ngrams(ngrams_counter, stop_words)
    return ngrams_counter

def get_ngrams(tweets, n, ngrams_to_remove):
    """Gets a list of ngrams from the collection of tweets and removes ngrams that appear in the list of ngrams_to_remove."""
    ngrams_list = []
    for index, tweet in tweets.iterrows():
        for sentence_words in tweet['sentences']:
            ngrams_list.extend(list(ngrams(sentence_words, n)))
    ngrams_list = [ngram for ngram in ngrams_list if ngram not in ngrams_to_remove]
    return ngrams_list