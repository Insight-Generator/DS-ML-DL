from celery import Celery
import pandas as pd
import os

broker = os.environ['RABBITMQ_BROKER']

app = Celery('proj',
             broker=broker,
            )

@app.task
def count_majority(csv_path):
    df = pd.read_csv(csv_path)
    output = []
    # TODO discuss output
    # [[column1: X], [column2: Y], [column3: Z]]