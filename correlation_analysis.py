from celery import Celery
import pandas as pd

app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             include=['proj.tasks'])

@app.task
def pearson_correlation(csv_path):
    # TODO Add another function to change to categorical
    df = pd.read_csv(csv_path)
    output = []

    for column in df:
        for other_column in df:
            corr_result = df[column].corr(df[other_column])
            if corr_result > .5 and corr_result < .999999999999: #.999... because of floating point precision. Some results that are perfectly correlated (1.0) end up as this
                if not any(corr_result in sublist for sublist in output): # Checks if corr_result already in output so no duplicate results
                    output.append([column, other_column, corr_result])

if __name__ == "__main__":
    app.start()