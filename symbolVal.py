import logging
from datetime import datetime, timedelta
import pandas as pd
import yFin


class SymbolVal:
    def __init__(self, year="2023"):
        # self.file_name = year + ".csv"
        self.target_symbols = "RUS_2000"
        self.data = ""
        self.year = year
        self.symbols = ""

    def evaluate(self):
        df = pd.read_csv(self.target_symbols)
        self.symbols = df['SYMBOL']
        new_symbols = []
        data = pd.DataFrame()
        i = 0
        try:
            for stock in self.symbols[i:]:
                yf = yFin.YFinance(ticker=stock, year=self.year)
                # print(yf.tail(1))
                data = yf.fetch_data()
                # print(data.tail(1))
                if len(data) > 0:
                    new_symbols.append(stock)

        except ValueError as value:
            print("value error: ", value)
        except ArithmeticError as ex:
            print("Exception : ArithmeticError occurred.")
        except Exception as ex:
            print("Exception occurred.", ex)

        print(new_symbols.__len__())
        df = pd.DataFrame(new_symbols, columns=['SYMBOL'])
        df.to_csv(str(self.year) + ".csv", index=False)

