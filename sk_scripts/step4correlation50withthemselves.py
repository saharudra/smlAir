import pandas as pd
import sklearn
import numpy
import matplotlib.pyplot as plt

df = pd.read_csv('top_50_feature_values.csv',index_col=0)

a = df.corr()
correlations = a
k = list()
k = df.columns.values
k = list(k)
names = k
# plot correlation matrix

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,50,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
# ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.ylabel('Feature Name')
plt.show()
a.to_csv('corrvaluesof50.csv')
