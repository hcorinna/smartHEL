import datetime
import pandas as pd
import matplotlib.pyplot as plt
import filter

def date_in_month(date, month, year):
    """Returns True if the given date is in the given month of the given year."""
    return date.year == year and date.month == month

def get_next_month(month, year):
    """Takes a month and year and returns the month and year of the following month."""
    if month < 12:
        return month + 1, year
    else:
        return 1, year + 1

def count_terms_monthly(trend_term, tweets, filtering_method):
    """
    Counts how often a term (trend_term) occurs each month in the collection of tweets.
    Checks the earliest date in the collection of tweets and the last date, then iterates over the months between those dates.
    For each month, the number of tweets that contain the trend_term are counted.
    """
    monthly_term_counter = {'date': [], 'counter': []}
    filtered_tweets = filtering_method(trend_term, tweets)
    if len(filtered_tweets) == 0:
        return "No tweets found for " + str(trend_term)
    earliest_tweet = min(filtered_tweets['datetime'])
    month = earliest_tweet.month
    year = earliest_tweet.year
    latest_tweet = max(filtered_tweets['datetime'])
    while month < latest_tweet.month or year < latest_tweet.year:
        counted = sum([date_in_month(dt, month, year) for dt in filtered_tweets.datetime])
        monthly_term_counter['date'].append(datetime.datetime(year, month, 1))
        monthly_term_counter['counter'].append(counted)
        month, year = get_next_month(month, year)
    return monthly_term_counter

def plot_history(trend_term, tweets, filtering_method):
    """Plots a word cloud based on a list of words."""
    term_history = count_terms_monthly(trend_term, tweets, filtering_method)
    if isinstance(term_history, str):
        # print error message
        print(term_history)
    else:
        term_history = pd.DataFrame(data=term_history)
        term_history.set_index('date', inplace=True)
        term_history.plot()
        plt.title(trend_term)
        plt.xlabel('Number of tweets')
        plt.ylabel('Time')
    
def plot_term_history(trend_term, tweets):
    """Plots how often a term (trend_term) was used per month in the tweets."""
    plot_history(trend_term, tweets, filter.by_search_term)
    
def plot_hashtag_history(hashtag, tweets):
    """Plots how often a hashtag was used per month in the tweets."""
    plot_history(hashtag, tweets, filter.by_hashtag)
    
def plot_ngram_history(ngram, tweets):
    """Plots how often an ngram was used per month in the tweets."""
    plot_history(ngram, tweets, filter.by_ngram)