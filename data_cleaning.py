import pandas as pd
import numpy as np
from scipy import stats

## Remove the data in the class label which has no class label
train_users="train_users_2.csv"
train_users_data=pandas.read_csv(train_users)
train_users_data=train_users_data[train_users_data.country_destination.notnull()]
train_users_features=list(train_users_data.columns.values)


age_gender_map=pandas.read_csv('age_gender_bkts.csv')
age_gender_features=list(age_gender_map.columns.values)

countries_data=pandas.read_csv('countries.csv')
countries_features=list(countries_data.columns.values)

sessions_data=pandas.read_csv('sessions.csv')
sessions_features=list(sessions_data.columns.values)

test_users_data=pandas.read_csv('test_users.csv')
test_users_features=list(test_users_data.columns.values)

all_features_list=set().union(train_users_features,age_gender_features,countries_features,sessions_features,test_users_features)

### If you want to verify if there are NaN values for a feature in a dataset, use the following syntax:
## sp.sum(sp.isnan(train_users_data.age))

## Fill in the missing values

#train_users_data[train_users_data.age.isnull()].age=stats.mode(train_users_data[train_users_data.age.notnull()].age)
train_users_data[train_users_data.age.isnull()].age=np.median(train_users_data[train_users_data.age.notnull()].age)

train_users_data[train_users_data.date_first_booking.isnull()].date_first_booking=stats.mode(train_users_data[train_users_data.date_first_booking.notnull()].date_first_booking).mode[0]

# Split first_activity_time as date time and make new features

train_users_data.time_first_active=pd.to_datetime(train_users_data.timestamp_first_active//1000000, format='%Y%m%d')
train_users_data.day=train_users_data.timestamp_first_active//1000000 - (train_users_data.timestamp_first_active//100000000)*100
train_users_data.part_of_month=pd.cut(train_users_data.day, 3, labels=["Start of month", "Mid month","End of month"])

train_users_data['first_affiliate_tracked']=train_users_data['first_affiliate_tracked'].replace(np.nan,'unknown')

ohe_features = ['gender','first_affiliate_tracked']
for f in ohe_features:
    train_users_data_dummy = pd.get_dummies(train_users_data[f], prefix=f)
    train_users_data = train_users_data.drop([f], axis=1)
    train_users_data = pd.concat((train_users_data, train_users_data_dummy), axis=1)

## If you want, you can delete the columns not required. For now, I am not deleting anything
