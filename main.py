import pandas as pd

df = pd.read_csv('tag_along.csv')

df['Tag Along'] = df['Tag Along'] * 100

df.to_excel('tag_along.xlsx', index=False)