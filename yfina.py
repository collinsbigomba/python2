import yfinance as yf
import pandas as pd

pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 8)
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

# dat = data.to_string(index=False)

tesla_data.reset_index(inplace=True)
tesla_data.to_string(index=False)
# print(tesla_data.count())
# print(tesla_data.columns)

print(tesla_data.head(5))



