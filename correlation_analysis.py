from celery import Celery
import pandas as pd
import os

broker = os.environ['RABBITMQ_BROKER']

app = Celery('proj',
             broker=broker,
            )

def check_convert_categorical(df):
    """Uses the first row to see if necessary to convert dataframe to categorical.
    Ex: if necessary, strings in each column will be converted to 0,1,etc. for every unique"""
    for column in df.iloc[:1].iteritems(): # df.iloc[:1] selects first header + first row
        if type(column[1][0]) == str: # checks if any of first row is string
            df[column[0]] = df[column[0]].astype('category').cat.codes

@app.task
def pearson_correlation(csv_path):
    # TODO Add another function to change to categorical
    # TODO download link for http => CSV. NOTE Awaiting download function
    df = pd.read_csv(csv_path)
    output = []

    check_convert_categorical(df)

    for column in df:
        for other_column in df:
            corr_result = df[column].corr(df[other_column])
            if corr_result > .5 and corr_result < .999999999999: #.999... because of floating point precision. Some results that are perfectly correlated (1.0) end up as this
                if not any(corr_result in sublist for sublist in output): # Checks if corr_result already in output arr. If not, append
                    output.append([column, other_column, corr_result])
    print(output)
    return output