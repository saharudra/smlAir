# DO NOT RUN, IT RUNS ON final_table.csv SIZE = 1.12 GB. final_table.csv is stored locally on Sarthak's system
# Opens final_table.csv and creates correlation csv wrt destination country

import pandas as pd

df = pd.read_csv('final_data_final.csv',index_col=0)
# y = pd.read_csv('destination.csv',header=None,index_col=0)
# y=y.rename(columns =  {1:'country_destination'})
#
# frames = [d,y]
# df = pd.concat(frames,1)
df = df.drop('id',axis=1)
a =df[df.columns[0:675]].apply(lambda x: x.corr(df['country_destination']))

print (a)
a.to_csv('Correlation.csv')

