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

    for column in df.iloc[:1].iteritems(): # df.iloc[:1] selects first header + first row
        if type(column[1][0]) == str:
            print(df[column[0]].value_counts())
            print("\n")
    # TODO discuss output
    # [[column1: X], [column2: Y], [column3: Z]]

    # Majority - if one category in column is taking >70%? (arbitrary %)

    # Above returns:
    # female    518
    # male      482
    # Name: gender, dtype: int64


    # group C    319
    # group D    262
    # group B    190
    # group E    140
    # group A     89
    # Name: race/ethnicity, dtype: int64


    # some college          226
    # associate's degree    222
    # high school           196
    # some high school      179
    # bachelor's degree     118
    # master's degree        59
    # Name: parental level of education, dtype: int64


    # standard        645
    # free/reduced    355
    # Name: lunch, dtype: int64


    # none         642
    # completed    358
    # Name: test preparation course, dtype: int64