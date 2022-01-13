# This configuration file is used to configure the data analys

# Strings to remove from tweets
our_stop_words = ['rt', '000', 'klo', '11', 'jotta', 'hyvää', '17', '18', 'fiksukalasatama', 'forum', 'hbh_hq', 'kyse', 'amp', 'siis', 'myös', 'kiitos', 'jo', 'näin', 'eli', 'sitten', 'vielä', 'joten', 'suoraan', 'enää', 'tänne', 'ajan', 'varmasti', 'oikein', 'jotain', 'vain', 'onko', 'taas', 'täältä', 'miten', 'ihan', 'kyllä', 'ok', 'mm', 'hyvä', 'ettei', 'new', 'us', 'tänään', 'lisää', 'täällä', 'siellä', '10', '15', '30', '12', 'ensi', 'aina', 'ensi', 'paljon', 'uusia', 'kaikki', 'tulee', 'ehkä', 'asiaa', 'asia', 'kautta', 'toki', 'juuri', 'tule', 'koko', 'ennen', 'uusi', 'aika', 'asiasta', 'tällä', 'kuten', 'ainakin', 'hei', 'voisi', 'kuitenkin', 'asti', 'vähän', 'mitään', 'eikä', 'mukana', 'viime', 'lisäksi', 'uutta', 'muuten', 'joku', 'jälkeen', 'aikana', 'eri', 'pian', 'hyvin', 'yksi', 'menee', 'esim', 'enemmän', 'huomenna']

# Words to remove when creating ngrams
ngram_stop_words = ['amp', 'rt']
# Words to remove when creating bigrams
bigrams_to_remove = [('in', 'the'), ('of', 'the'), ('at', 'the'), ('to', 'the'), ('on', 'the')]
# Words to remove when creating trigrams
trigrams_to_remove = []
# Words to remove when creating fourgrams
fourgrams_to_remove = []