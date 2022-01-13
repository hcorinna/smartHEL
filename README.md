# Methods for uncovering discourses that shape the urban imaginary in Helsinki's smart city

This repository is the official implementation of the paper "Methods for uncovering discourses that shape the urban imaginary in Helsinki's smart city".
The paper explores how the city of Helsinki shapes the discourse around smart and sustainable city development, including subjectivities and conceptualizations of agency.
We utilize Foucauldian Discourse Analysis (FDA) to identify which discourses are elevated, and which are silenced, through statements posted on the social media platform Twitter.
This repository provides the code for the analysis of the data collected from Twitter.

## Requirements

You should have Python (ideally [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)) installed. The code has been built and tested with Python 3.7.9 with Anaconda 4.10.3.

If you use ``conda``, you can create a virtual environment from the ``environment.yml`` file. The name of the environment will be ``smartHEL``.

```setup
conda env create -f environment.yml
conda activate smartHEL
```

If you do not have conda installed, you may also install the required packages through ``pip``:

```setup
pip install -r requirements.txt
```

We recommend setting up a [virtual environment](https://docs.python.org/3/library/venv.html) for these dependencies.

## Data

We collected tweets and retweets by accounts directly linked to the City of Helsinki's smart and green agendas.
For each account, all of their posts were pulled starting from their respective join date until May 25th, 2021.
We have obtained the data through queries to the [Twitter API for Acadamic Research](https://developer.twitter.com/en/products/twitter-api/academic-research), using [tweetsearcher](https://github.com/DigitalGeographyLab/tweetsearcher).
The license with which we collected data from Twitter does not allow us to share this data.
Therefore, the data file is not included and the notebooks only show aggregate statistics, such as most common tweets, instead of individual tweets.

## Analysis

The results of the analysis can be found in the notebooks.
The `.py` files provide the code necessary to run the Jupyter Notebooks.
If you want to run the notebooks, make sure you first add a data file.