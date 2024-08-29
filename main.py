import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print('starting...')

df = pd.read_csv(
    "ts_course_data/book_sales.csv",
    index_col='Date',
    parse_dates=['Date'],    
).drop('Paperback', axis=1)

df['Lag_1'] = df['Hardcover'].shift(1)
df = df.reindex(columns=['Hardcover', 'Lag_1'])

print(df.head())