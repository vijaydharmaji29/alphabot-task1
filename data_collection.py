import pandas as pd
import math
import numpy as np
from datetime import datetime

#function to calculate log returns for the given period
def calculate_log_returns(d, period):
    close = d.close
    returns = []
    for i in range(len(close)):
        if i < period: #for sessions we can't calculate log returns
            returns.append(None)
            continue
        returns.append(math.log10(d.iloc[i].close / d.iloc[i - period].close))

    return np.array(returns)

def create_data(df):
    df = df.astype({'datetime': 'string'})
    df['date'] = df.datetime.str[:10]  # craeting a column for only the date

    df = df.drop_duplicates(subset=['date'],
                            keep='last')  # dropping same dates so we have daily intervals instead of per min

    #adding log returns
    df['5day_log_returns'] = calculate_log_returns(df, 5)
    df['13day_log_returns'] = calculate_log_returns(df, 13)
    df['20day_log_returns'] = calculate_log_returns(df, 20)

    df['month'] = df.datetime.str[:7]
    df = df.drop_duplicates(subset=['month'],
                            keep='first')


    df = df.dropna()

    return df

#main function for this file, returns pandas dataframe with all required columns calculated
def get_data(path):
    df = pd.read_csv('big_data/' + path)
    df = create_data(df)

    return df


if __name__ == '__main__':
    df = get_data('ASIANPAINT.csv')
    print(df.head(10))