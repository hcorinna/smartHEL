from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_cloud(words):
    """Plots a word cloud based on a list of words."""
    wordcloud_data = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False).generate(" ".join(words))
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud_data) 
    plt.axis("off");