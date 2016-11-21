# DO NOT RUN, IT RUNS ON final_table.csv SIZE = 1.12 GB. final_table.csv is stored locally on Sarthak's system
# Opens final_table.csv and creates correlation csv wrt destination country

import pandas as pd

df = pd.read_csv('final_table.csv')
a = (df[df.columns[2:1318]].apply(lambda x: x.corr(df['country_destination'])))
print (a)
a.to_csv('Correlation.csv')

