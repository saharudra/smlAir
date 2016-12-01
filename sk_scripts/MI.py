import pandas as pd
import matplotlib.pyplot as plt
from sklearn import feature_selection as fs
import sklearn

df = pd.read_csv('top_50_feature_values.csv',index_col=0,header=None)
k= sklearn.metrics.mutual_info_score(df,df)
print (k)