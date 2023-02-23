import os

import pandas as pd
import data_collection as dc

tickers = os.listdir('big_data/')

print('GETTING STOCK DATA')

stocks_data = {}

#getting data for all stocks in the timeframe
for t in tickers:
    ticker_data = dc.get_data(t)
    stocks_data[t] = ticker_data

def next(index):

    if index < len(stocks_data[tickers[0]]):
        data = {
            'symbol': [], '5day': [], '13day': [], '20day': [], 'close': [], 'date': []
        }

        for t in tickers:
            symbol = stocks_data[t].iloc[index].symbol
            day5 = stocks_data[t].iloc[index]['5day_log_returns']
            day13 = stocks_data[t].iloc[index]['13day_log_returns']
            day20 = stocks_data[t].iloc[index]['20day_log_returns']
            close = stocks_data[t].iloc[index]['close']
            date = stocks_data[t].iloc[index]['date']

            data['symbol'].append(symbol)
            data['5day'].append(day5)
            data['13day'].append(day13)
            data['20day'].append(day20)
            data['close'].append(close)
            data['date'].append(date)


        df = pd.DataFrame(data, index=data['symbol'])

        return df

    return None

if __name__ == '__main__':
    print('STARTING')
    print(next(20))
    print("************")
    print(next(40))