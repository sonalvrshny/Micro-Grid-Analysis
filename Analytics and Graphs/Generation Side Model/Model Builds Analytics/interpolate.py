import pandas as pd

df = pd.read_csv('output.csv')
df = df.interpolate(method='piecewise_polynomial', axis=0)
df = df.set_index('Date/Time')
df.to_csv('interpolated.csv')