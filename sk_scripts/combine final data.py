import pandas as pd

train = pd.read_csv('final_table.csv',index_col=0)
test = pd.read_csv('final_test.csv',index_col=0)
y = train['country_destination']
train = train.drop('country_destination',1)
a = train.columns.values
b = test.columns.values
c = set(a).intersection(b)
d = list()
d = list(d)
e = set(a)-set(b)
f = list()
f = e
f = list(f)
f1 = train[d]
f2 = train[f]
f3 = y
frames = [f1,f2,f3]
final_data_combined = pd.concat(frames,axis = 1)
final_data_combined.to_csv('final_data_combined.csv')
f1.to_csv('common_features_test_train.csv')