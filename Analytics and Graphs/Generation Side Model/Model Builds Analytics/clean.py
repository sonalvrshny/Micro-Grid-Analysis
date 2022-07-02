import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('enphase.csv')
df_data_time = []
for i in df['Date/Time']:
    df_data_time.append(pd.Timestamp(i.split(' +')[0]))
df['Date/Time'] = df_data_time

df_date = pd.date_range('2019-04-03 00:00:00', '2019-04-09 00:00:00', freq='5min')
idx = pd.DatetimeIndex(df_date)
df = df.set_index('Date/Time')
df = df.reindex(idx)
df.index.name = 'Date/Time'
df.to_csv('output.csv')
#  after cleaning open csv file and add 0s at the starting till 1st value is encountered
