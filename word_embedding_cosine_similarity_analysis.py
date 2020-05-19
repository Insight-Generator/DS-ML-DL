from celery import Celery
import pandas as pd
import os

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

@app.task
def cosine_similarity(entry1, entry2):
    """Will do cosine similarity based on the two entries being compared. Generally sees how
    correlated the two entries are.
    Ex1: Sex and Gender are highly correlated b/c similar meaning
    Ex2: Ice and Cream are highly correlated b/c commonly used together"""
    pass