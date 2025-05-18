import backtrader as bt

class BollingerBandStrategy(bt.Strategy):
    params = (
        ("period", 20),
        ("devfactor", 2.0),
    )

    def __init__(self):
        self.bb = bt.indicators.BollingerBands(period=self.params.period, devfactor=self.params.devfactor)

    def next(self):
        if not self.position:
            if self.data.close[0] < self.bb.lines.bot[0]:
                self.buy()
        else:
            if self.data.close[0] > self.bb.lines.top[0]:
                self.sell()

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(BollingerBandStrategy)

    data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                      fromdate=datetime(2020, 1, 1),
                                      todate=datetime(2021, 1, 1))
    cerebro.adddata(data)

    cerebro.broker.set_cash(10000)
    cerebro.run()
    cerebro.plot()
