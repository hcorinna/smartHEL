import pickle
import datetime
import re
from nltk.tokenize import RegexpTokenizer
from nltk import tokenize

def get_data(remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Returns cleaned data."""
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f) 
    data = clean_data(data, remove_mentions, remove_hashtags, remove_urls)
    return data

def get_date(date_string):
    """Converts date string into datetime format for further processing."""
    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.000%z")

def clean_data(data, remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Cleans the raw data."""
    data['datetime'] = data.apply(lambda tweet: get_date(tweet['created_at']), axis=1)
    data['sentences'] = data.apply(lambda tweet: split_into_sentences(tweet, remove_mentions, remove_hashtags, remove_urls), axis=1)
    return data

def split_into_sentences(tweet, remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Splits a cleaned tweet into an array of sentences. Each sentence is represented by an array of words."""
    tokenizer = RegexpTokenizer(r'\w+')
    cleaned_text = clean_tweet(tweet, remove_mentions, remove_hashtags, remove_urls)
    sentences = []
    for sentence in tokenize.sent_tokenize(cleaned_text):
        sentence_words = tokenizer.tokenize(sentence)
        if len(sentence_words) > 0:
            sentences.append(sentence_words)
    return sentences

def clean_tweet(tweet, remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Cleans a single tweet by removing words, converting words into a normalized form etc."""
    cleaned_text = remove_entities(tweet, remove_mentions, remove_hashtags, remove_urls)
    cleaned_text = cleaned_text.lower()
    if remove_urls:
        # Twitter's URL entities don't contain all URLs, so we remove more URLs in this step
        cleaned_text = re.sub(r"http\S+", "", cleaned_text)
    cleaned_text = re.sub("09 310 [0-9]+", "servicenumber", cleaned_text)
    cleaned_text = re.sub("helsingin", "helsinki", cleaned_text)
    cleaned_text = re.sub("helsingissä", "helsinki", cleaned_text)
    cleaned_text = re.sub("kaupungin", "kaupunki", cleaned_text)
    cleaned_text = re.sub("tiedon", "tieto", cleaned_text)
    cleaned_text = re.sub("tietoa", "tieto", cleaned_text)
    cleaned_text = re.sub("vuotta", "vuosi", cleaned_text)
    cleaned_text = re.sub("vuonna", "vuosi", cleaned_text)
    cleaned_text = re.sub("vuoden", "vuosi", cleaned_text)
    cleaned_text = re.sub("tehdään", "tehdä", cleaned_text)
    cleaned_text = re.sub("laitetaan", "laittaa", cleaned_text)
    cleaned_text = re.sub("cities", "city", cleaned_text)
    cleaned_text = re.sub("alueella", "alueen", cleaned_text)
    # This will turn something like "the world's" into "the world" because "world" and "s" will otherwise be seen as 2 separate words.
    cleaned_text = re.sub("'", "", cleaned_text)
    return cleaned_text

def remove_entities(tweet, remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """
    Twitter's API returns a list of mentions, hashtags and URLs for each tweet.
    For each of these entities the string is known as well as the position of this string in the text.
    This function uses this information to remove such entities.
    Whether entities should be removed can be decided by entity type (mention, hashtag, URL) through the respective input arguments.
    """
    potential_entities_list = []
    if remove_mentions:
        potential_entities_list.append(tweet['entities.mentions'])
    if remove_hashtags:
        potential_entities_list.append(tweet['entities.hashtags'])
    if remove_urls:
        potential_entities_list.append(tweet['entities.urls'])
    
    entities = []
    for potential_entities in potential_entities_list:
        if potential_entities != None:
            entities.extend(potential_entities)
            
    entities = sorted(entities, key=lambda element: element['start'])
    cleaned_tweet = ''
    start = 0
    for e in range(len(entities)):
        cleaned_tweet += tweet['text'][start:entities[e]['start']]
        cleaned_tweet += '.'
        start = entities[e]['end']
    cleaned_tweet += tweet['text'][start:len(tweet['text'])]
    return cleaned_tweet

def get_original_tweets(remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Returns the cleaned data, but only the original tweets, i.e., no retweets."""
    data = get_data(remove_mentions, remove_hashtags, remove_urls)
    original_tweets = data.loc[data['referenced_tweets.type'] != 'retweeted']
    return original_tweets

def get_retweets(remove_mentions=True, remove_hashtags=True, remove_urls=True):
    """Returns the cleaned data, but only the retweets."""
    data = get_data(remove_mentions, remove_hashtags, remove_urls)
    retweets = data.loc[data['referenced_tweets.type'] == 'retweeted']
    return retweets