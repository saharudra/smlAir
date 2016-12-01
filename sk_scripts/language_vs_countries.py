import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('train_users_2.csv')
y = pd.read_csv('destination.csv',index_col=0,header=None)

language = train['language']
frames = [y,language]
yl = pd.concat(frames,axis = 1)  # df with language and destination country
yl.columns = ['country_destination','language']
# yl = pd.read_csv('yl.csv',index_col=0)
print (yl)
# yl.hist()
langlist = set(yl['language'])
# # # print (top_50_features)
# # # top_50_features.to_csv('top_50_features.csv')
print (yl['language'].value_counts())  # count for language
yl.hist()
plt.xlabel('Country_destination')
plt.ylabel('Language')
plt.show()

# print ('1')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax2 = ax.twinx()
# print ('2')
# yl['country_destination'].plot(kind='bar', color='red', ax=ax, position=0, width=0.25)
# print ('3.1')
# yl['language'].plot(kind='bar', color='blue', ax=ax2, position=1, width=0.25)
# print ('3.2')
# ax.set_ylabel = ('change1')
# ax2.set_ylabel = ('change2')
# print ('4')
# plt.show()

le = preprocessing.LabelEncoder()
le.fit(list(set(train.country_destination)))
train.country_destination = le.transform(train.country_destination)