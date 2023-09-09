from datetime import datetime, timedelta
import logging
import yfinance as yf


class YFinance:
    def __init__(self, ticker="^NSEI", period="1000d", interval="1d", data_location=None, country="India", year="2013"):
        self.data = None
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.country = country
        # self.file_name = data_location + ticker.upper() + ".csv"
        self.year = year

        '''
        if ticker[0] == '^':
            self.file_name = data_location + ticker[1:].upper() + ".csv"
        else:
            self.file_name = data_location + ticker.upper() + ".csv"
        '''

    def fetch_data(self):
        now = datetime.now() + timedelta(days=1)
        end_date = now.strftime("%Y-%m-%d")
        start_date = str(self.year) + "-01-01"
        end_date = str(self.year) + "-01-05"

        # print(end_date)
        if self.ticker == "SPY" or self.ticker == "^NSEI":
            self.data = yf.download(tickers=self.ticker, period=self.period, interval=self.interval, start="2022-01-01",
                                    end=end_date)
        else:
            self.data = yf.download(tickers=self.ticker, period=self.period, interval=self.interval, start=start_date,
                                    end=end_date)
        return self.data

