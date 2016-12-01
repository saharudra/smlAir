import pandas as pd
import sklearn
import numpy as np
df = pd.read_csv('final_data_final.csv',index_col=0)
df2 = pd.read_csv('Top_50_features.csv',index_col=0)
df3= df[df2.index]
print (df3)
df3.to_csv('top_50_feature_values.csv')