import pandas as pd
import numpy as np
from sklearn import preprocessing

def encodeage():
    print("in encodeage")
    bins = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 120])
    group_names = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', \
                   '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100+']
    train_users_data['age_bucket']=pd.cut(train_users_data.age.astype(int), bins, labels=group_names)
    test_users_data['age_bucket'] = pd.cut(test_users_data.age.astype(int), bins, labels=group_names)

def fix_age():
    print("in fix_age")
    ## AirBnB allows users who are 18 and older
    train_users_data.age[train_users_data.age < 18] = np.nan
    train_users_data.age[train_users_data.age > 1998] = np.nan
    train_users_data.age[train_users_data.age > 1896] = 2016 - train_users_data.age
    train_users_data.age[train_users_data.age > 120] = np.nan
    train_users_data.ix[train_users_data.age.isnull(), 'age'] = np.median(train_users_data[train_users_data.age.notnull()].age)
    #train_users_data['young'] = np.where(train_users_data['age'] <= 50, 1, 0)
    test_users_data.age[test_users_data.age < 18] = np.nan
    test_users_data.age[test_users_data.age > 1998] = np.nan
    test_users_data.age[test_users_data.age > 1896] = 2016 - test_users_data.age
    test_users_data.age[test_users_data.age > 120] = np.nan
    test_users_data.ix[test_users_data.age.isnull(), 'age'] = np.median(\
        test_users_data[test_users_data.age.notnull()].age)


def fix_gender():
    print("in fix_gender")
    train_users_data.gender[train_users_data.gender == '-unknown-'] = np.nan
    test_users_data.gender[test_users_data.gender == '-unknown-'] = np.nan

def fill_missing_values():
    sessions_data.ix[sessions_data.secs_elapsed.isnull(), 'secs_elapsed'] = np.median(sessions_data[sessions_data.secs_elapsed.notnull()].secs_elapsed)

def encode_country_destination():
    print("in encode_country_destination")
    le = preprocessing.LabelEncoder()
    le.fit(list(set(train_users_data.country_destination)))
    train_users_data.country_destination = le.transform(train_users_data.country_destination)


train_users="train_users_2.csv"
train_users_data=pd.read_csv(train_users)
train_users_data=train_users_data[train_users_data.country_destination.notnull()]
train_users_features=list(train_users_data.columns.values)
train_users_data['date_first_booking']=pd.to_datetime(train_users_data['date_first_booking'])

sessions_data=pd.read_csv('sessions.csv')
sessions_features=list(sessions_data.columns.values)

test_users_data=pd.read_csv('test_users.csv')
test_users_features=list(test_users_data.columns.values)

fix_age()
fix_gender()

train_users_data['date_first_active']=pd.to_datetime(train_users_data.timestamp_first_active//1000000, format='%Y%m%d')
train_users_data['date_in_month']=train_users_data.timestamp_first_active//1000000 - (train_users_data.timestamp_first_active//100000000)*100
train_users_data['part_of_month']=pd.cut(train_users_data.date_in_month, 3, labels=["Start of month", "Mid month","End of month"])
train_users_data['month']=(train_users_data.timestamp_first_active//100000000) - (train_users_data.timestamp_first_active//10000000000*100)

train_users_data.timestamp_first_active=train_users_data.timestamp_first_active.astype(str)
train_users_data['active_hours']=train_users_data.timestamp_first_active.str[8:10].astype(int)

bins=[0,6,10,15,19,23]
group_names=["Late night","Early Morning","Mid Day","Afternoon","Evening"]
train_users_data['daypart']=pd.cut(train_users_data['active_hours'],bins,labels=group_names)

train_users_data['first_affiliate_tracked']=train_users_data['first_affiliate_tracked'].replace(np.nan,'-1')


sLength=len(train_users_data['age'])
train_users_data['age_bucket'] = pd.Series(np.empty(sLength, dtype=object), index=train_users_data.index)

"""
SAME STEPS FOR TEST DATA
"""
test_users_data['date_first_booking']=pd.to_datetime(test_users_data['date_first_booking'])
test_users_data.date_account_created=pd.to_datetime(test_users_data.date_account_created)

test_users_data['date_first_active']=pd.to_datetime(test_users_data.timestamp_first_active//1000000, format='%Y%m%d')
test_users_data['date_in_month']=test_users_data.timestamp_first_active//1000000 - (test_users_data.timestamp_first_active//100000000)*100
test_users_data['part_of_month']=pd.cut(test_users_data.date_in_month, 3, labels=["Start of month", "Mid month","End of month"])
test_users_data['month']=(test_users_data.timestamp_first_active//100000000) - (test_users_data.timestamp_first_active//10000000000*100)
test_users_data.timestamp_first_active=test_users_data.timestamp_first_active.astype(str)
test_users_data['active_hours']=test_users_data.timestamp_first_active.str[8:10].astype(int)
bins=[0,6,10,15,19,23]
group_names=["Late night","Early Morning","Mid Day","Afternoon","Evening"]
test_users_data['daypart']=pd.cut(test_users_data['active_hours'],bins,labels=group_names)
test_users_data['daypart']=test_users_data['daypart'].astype(object)
test_users_data['daypart'].fillna(-1, inplace=True)
test_users_data['first_affiliate_tracked']=test_users_data['first_affiliate_tracked'].replace(np.nan,'-1')

sLength=len(test_users_data['age'])
test_users_data['age_bucket'] = pd.Series(np.empty(sLength, dtype=object), index=test_users_data.index)

encodeage()

train_users_data['daypart']=train_users_data['daypart'].astype(object)
train_users_data['daypart'].fillna(-1, inplace=True)

fill_missing_values()

sessions_data.rename(columns = {'user_id': 'id'}, inplace=True)
sessions_data['action'].fillna(-1, inplace=True)
sessions_data['action_type'].fillna(-1, inplace=True)
sessions_data['action_detail'].fillna(-1, inplace=True)

bins = [0,10800,21600,43200,86400,172800,1799949]  #172800 = 48 hours
group_names=["Very_less","Less","Descent","More","High","Very_high"]
sessions_data['secs_elapsed_categories']=pd.cut(sessions_data['secs_elapsed'].astype(int),bins,labels=group_names)


#action_table
action = pd.DataFrame(pd.pivot_table(sessions_data, values='secs_elapsed_categories', index='id', columns='action', aggfunc=len, fill_value=0))
action.rename(columns=lambda x: 'action_'+str(x), inplace=True)
action.reset_index( inplace=True)

#action_detail_table
action_detail = pd.DataFrame(pd.pivot_table(sessions_data, values='secs_elapsed_categories', index='id', columns='action_detail', aggfunc=len, fill_value=0))
action_detail.rename(columns=lambda x: 'action_detail_'+str(x), inplace=True)
action_detail.reset_index( inplace=True)

#action_type_table
action_type = pd.DataFrame(pd.pivot_table(sessions_data, values='secs_elapsed_categories', index='id', columns='action_type', aggfunc=len, fill_value=0))
action_type.rename(columns=lambda x: 'action_type_'+str(x), inplace=True)
action_type.reset_index( inplace=True)

#device_type_table
device_type = pd.DataFrame(pd.pivot_table(sessions_data, values='secs_elapsed_categories', index='id', columns='device_type', aggfunc=len, fill_value=0))
device_type.rename(columns=lambda x: 'device_type_'+str(x), inplace=True)
device_type.reset_index( inplace=True)

#seconds_elapsed_table
secs_elapsed = pd.DataFrame(pd.pivot_table(sessions_data, values='secs_elapsed', index='id', columns='secs_elapsed_categories', aggfunc=len, fill_value=0))
secs_elapsed.rename(columns=lambda x: 'secs_elapsed_'+str(x), inplace=True)
secs_elapsed.reset_index( inplace=True)

grouped = sessions_data[['id', 'action']].groupby('id')
fun1 = lambda x: len(pd.Series(x).value_counts())
action_num = grouped.aggregate(fun1)
action_num = pd.DataFrame(action_num)
action_num.reset_index( inplace=True)

#del sessions_data['secs_elapsed']

sessions_table = pd.merge(action, action_detail,'left', on=['id'])
sessions_table = pd.merge(sessions_table,action_type,'left', on=['id'])
sessions_table = pd.merge(sessions_table,device_type,'left', on=['id'])
sessions_table = pd.merge(sessions_table,secs_elapsed,'left', on=['id'])
sessions_table = pd.merge(sessions_table,action_num,'left', on=['id'])

train_users_data = pd.merge(left=train_users_data,right = sessions_table, on=['id'], how='left')

ohe_features = ['age_bucket', 'language','part_of_month','daypart','gender','first_affiliate_tracked', \
                'affiliate_channel','affiliate_provider','first_browser','first_device_type', \
                'signup_app','signup_method']


for f in ohe_features:
    train_users_data_dummy = pd.get_dummies(train_users_data[f], prefix=f)
    train_users_data = train_users_data.drop([f], axis=1)
    train_users_data = pd.concat((train_users_data, train_users_data_dummy), axis=1)

for f in ohe_features:
    test_users_data_dummy = pd.get_dummies(test_users_data[f], prefix=f)
    test_users_data = test_users_data.drop([f], axis=1)
    test_users_data = pd.concat((test_users_data, test_users_data_dummy), axis=1)

test_users_data = pd.merge(left=test_users_data,right = sessions_table, on=['id'], how='left')

encode_country_destination()
