# パッケージ
import pandas_datareader.data as pdr

import yfinance as yf

yf.pdr_override()

# 株価情報の取得
df = pdr.get_data_yahoo("9020.T", start='2010-01-01')

print(df)