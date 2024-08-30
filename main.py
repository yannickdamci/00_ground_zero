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

fig, ax = plt.subplots()
ax = sns.regplot(x='Lag_1', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_aspect('equal')
ax.set_title('Lag Plot of Hardcover Sales')

plt.show()