import data_giver as dg
import pandas as pd

class action(object):
    def __init__(self, ticker, qty, buy, sell, buy_val, sell_val, date):
        self.ticker = ticker
        self.qty = qty
        self.buy = buy
        self.sell = sell
        self.buy_val = buy_val
        self.sell_val = sell_val
        self.date = date

    def show(self):
        print(self.ticker, self.buy,
              self.sell, self.buy_val, self.sell_val)


def calculate(capital, df, positions):
    buys = []
    execute = []

    for i in positions:
        sell_val = i.qty*df.loc[i.ticker]['close']
        new_action = action(i.ticker, i.qty, False, True, 0, sell_val, df.loc[i.ticker]['date'])
        execute.append(new_action)

    for i in range(len(df)):
        if df.iloc[i]['5day'] > df.iloc[i]['20day'] and df.iloc[i]['5day'] > df.iloc[i]['13day']:
            buys.append(df.iloc[i]['symbol'])

    capital_each_stock = capital/len(buys)
    for i in buys:
        qty = int(capital_each_stock/df.loc[i]['close'])
        buy_val = qty*df.loc[i]['close']
        new_action = action(i, qty, True, False, buy_val, 0, df.loc[i]['date'])
        execute.append(new_action)

    return execute



if __name__ == '__main__':
    calculate(2)
    pass
