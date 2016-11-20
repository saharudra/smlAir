import pandas as pd

df = pd.read_csv('final_table.csv')
a = (df[df.columns[2:1318]].apply(lambda x: x.corr(df['country_destination'])))
print (a)
a.to_csv('Correlation.csv')

