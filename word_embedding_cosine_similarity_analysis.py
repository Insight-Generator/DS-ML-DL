from celery import Celery
import pandas as pd
import os

import scipy
import re
from nltk.corpus import stopwords
import pandas as pd

broker = os.environ['RABBITMQ_BROKER']

app = Celery('proj',
             broker=broker,
            )

# Section to load model. Done globally so message queue only loads once
import numpy as np

model_location = 'pretrained_embeddings/glove.6B/glove.6B.200d.txt' # TODO change location in production
glove_model = {}
with open(model_location, encoding="utf8" ) as f:
    section = f.readlines()
    
for line in section:
    split_line = line.split(" ")
    word = split_line[0]
    if word.isalpha(): # Will be used to only keep the words in embeddings
        embedding = np.array([float(val) for val in split_line[1:]]) # 1: for only the embeddings. Reference Note1
        glove_model[word] = embedding

def preprocess(raw_text):
    # keep only words
    letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)
    
    # convert to lower case and split 
    words = letters_only_text.lower().split()

    # remove stopwords
    stopword_set = set(stopwords.words("english"))
    cleaned_words = list(set([w for w in words if w not in stopword_set]))
    return cleaned_words

def cosine_distance_between_two_words(word1, word2):
    return (1- scipy.spatial.distance.cosine(glove_model[word1], glove_model[word2]))

@app.task
def cosine_similarity(entry1, entry2):
    """Will do cosine similarity based on the two entries being compared. Generally sees how
    similar the two entries are.
    Ex1: Sex and Gender are highly similar b/c similar meaning
    Ex2: Ice and Cream are highly similar b/c commonly used together
    
    Returns single boolean based on if any result > .5 (arbitrary)
         cream      WORD2
    ice  0.546036   0.641752
    """

    entry1 = preprocess(entry1)
    entry2 = preprocess(entry2)
    result_list = [[cosine_distance_between_two_words(word1, word2) for word2 in entry2] for word1 in entry1]
    return any([corr > .5 for group in result_list for corr in group])