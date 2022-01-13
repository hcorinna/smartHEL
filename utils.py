from config import our_stop_words
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords

author_ids = ['87397938', '3197786830', '1379860454', '733684440317190145', '738050260799475713', '2435241757']

authors = {
    '87397938': 'ForumViriumHelsinki',
    '3197786830': 'Fiksu Kalasatama',
    '1379860454': 'HelsinkiBusinessHub',
    '733684440317190145': 'Helsinki Smart Region',
    '738050260799475713': 'Smart & Clean',
    '2435241757': 'Helsingin ilmastoteot'}

def get_hashtags(tweets):
    """Returns a lowercase list of all hashtags used in all tweets. Each occurrence of a hashtag appears in the list,
    so it will likely (and intentionally) include duplicates."""
    hashtag_entities = [hashtag['tag'].lower() for potential_hashtags in tweets['entities.hashtags'] if potential_hashtags != None for hashtag in potential_hashtags]
    return hashtag_entities

def get_tweets_by_authors(tweets, author_ids):
    """
    Takes tweets and sorts them into a dictionary based on the author_ids.
    Only tweets are included whose author ID appears in the list of author_ids.
    """
    tweets_by_author = {}
    for author_id in author_ids:
        # find tweet with that author
        author_tweets = tweets[tweets['author_id'] == author_id]
        tweets_by_author[author_id] = author_tweets
    return tweets_by_author

def tweets_to_words(tweets):
    """
    Takes tweets and creates a list of all the words occurring in the tweets.
    Therefore, duplicates are likely and intentional.
    The tweets have already been cleaned and split into sentences / words at this point.
    Words are removed if they are just a single letter or appear in any of the stop word lists (English, Finnish and our own).
    """
    words = [word for index, tweet in tweets.iterrows() for sentence_words in tweet['sentences'] for word in sentence_words]
    stop_words_en = set(stopwords.words('english')) 
    stop_words_fi = set(stopwords.words('finnish'))
    # Filtering out words in the English, Finnish and our list of stop words. Also filtering out words that are just a single letter.
    words = [w for w in words if not w in stop_words_en and not w in stop_words_fi and not w in our_stop_words and not len(w)==1] 
    return words