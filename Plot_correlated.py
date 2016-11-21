# opens correlation.csv and creates top_50_features.csv and also plots the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Correlation.csv', header=None)
df = df.sort_values(1,ascending=False)
top_50_features = df[1:51]
top_50_features.columns = ['Feature Name','Correlation Value']
top_50_features.plot.bar(color = 'g')
print (top_50_features)
top_50_features.to_csv('top_50_features.csv')
plt.xlabel('Feature column number (numbering of final table)')
plt.ylabel('Correlation Value')
plt.show()