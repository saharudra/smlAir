import pandas as pd
import numpy as np
from scipy import stats
import copy

def formatgender():
    for index, row in age_gender_map.iterrows():
        if age_gender_map.loc[index]['gender'] == "male":
            age_gender_map.ix[index,'gender'] = "MALE"
        elif age_gender_map.loc[index]['gender'] == "female":
            age_gender_map.ix[index, 'gender'] = "FEMALE"

def add_values_agb():
    global age_gender_map
    other_countries=set(train_users_data.country_destination)-set(age_gender_map.country_destination)
    other_gender=set(train_users_data.gender)-set(age_gender_map.gender)
    bkts = set(age_gender_map.age_bucket)
    for country in set(train_users_data.country_destination):
        for gender in other_gender:
            for k in bkts:
                newrow = pd.DataFrame([[k, country, gender, '', '']], columns=list(age_gender_map.columns))
                age_gender_map = age_gender_map.append(newrow, ignore_index=True)
    for country in other_countries:
        for gender in other_gender:
            for k in bkts:
                newrow=pd.DataFrame([[k, country, gender, '', '']], columns=list(age_gender_map.columns))
                ge_gender_map = age_gender_map.append(newrow, ignore_index=True)
    for country in other_countries:
        for gender in other_gender:
            for k in bkts:
                newrow = pd.DataFrame([[k, country, gender, '', '']], columns=list(age_gender_map.columns))
                age_gender_map = age_gender_map.append(newrow, ignore_index=True)

## encodeage performed on train_users_data and age_gender_bkts.csv
## if n=0, encode train_users_data
## if n=1, encode age_gender_bkts
def encodeage():
    for index, row in train_users_data.iterrows():
        age=int(train_users_data.loc[index]['age'])
        if (age>=0) and (age<5):
            updated_age="0-4"
        elif (age>=5) and (age<10):
            updated_age="5-9"
        elif (age >= 10) and (age < 15):
            updated_age = "10-14"
        elif (age >= 15) and (age < 20):
            updated_age = "15-19"
        elif (age>=20) and (age<25):
            updated_age="20-24"
        elif (age>=25) and (age<30):
            updated_age="25-29"
        elif (age>=30) and (age<35):
            updated_age="30-34"
        elif (age>=35) and (age<40):
            updated_age="35-39"
        elif (age>=40) and (age<45):
            updated_age="40-44"
        elif (age>=45) and (age<50):
            updated_age="45-49"
        elif (age>=50) and (age<55):
            updated_age="50-54"
        elif (age >= 55) and (age < 60):
            updated_age = "55-59"
        elif (age>=60) and (age<65):
            updated_age="60-64"
        elif (age>=65) and (age<70):
            updated_age="65-69"
        elif (age>=70) and (age<75):
            updated_age="70-74"
        elif (age>=75) and (age<80):
            updated_age="75-79"
        elif (age>=80) and (age<85):
            updated_age="80-84"
        elif (age >= 85) and (age < 90):
            updated_age = "85-89"
        elif (age>=90) and (age<95):
            updated_age="90-94"
        elif (age >= 95) and (age < 100):
            updated_age = "95-99"
        else:
            updated_age="100+"
        train_users_data.ix[index,'age_bucket']=updated_age

def add_missing_age_gender_data():
    global age_gender_map
    bkts=set(age_gender_map.age_bucket)
    for k in bkts:
        newrow = pd.DataFrame([[k, 'NDF', 'MALE', '', ''], [k, 'other', 'MALE', '', ''],[k, 'NDF', 'FEMALE', '', ''], [k, 'other', 'FEMALE', '', '']], columns=list(age_gender_map.columns))
        age_gender_map = age_gender_map.append(newrow, ignore_index=True)

def del_duplicate_columns():
    del train_users_data['gender']
    del train_users_data['time_first_active']
    del train_users_data['age']
    del age_gender_map['age_bucket']
    del age_gender_map['gender']
    del age_gender_map['country_destination']


#############################################
#                                           #
#               MAIN FUNCTION               #
#                                           #
#############################################

## Remove the data in the class label which has no class label
train_users="train_users_2.csv"
train_users_data=pd.read_csv(train_users)
train_users_data=train_users_data[train_users_data.country_destination.notnull()]
train_users_features=list(train_users_data.columns.values)


age_gender_map=pd.read_csv('age_gender_bkts.csv')
age_gender_features=list(age_gender_map.columns.values)

add_missing_age_gender_data()

countries_data=pd.read_csv('countries.csv')
countries_features=list(countries_data.columns.values)

## Appending column for NDF country destination

newrow=pd.DataFrame([['NDF','','','','','','',],['other','','','','','','',],['-unknown-','','','','','','',]],columns=list(countries_data.columns))
countries_data=countries_data.append(newrow, ignore_index=True)

sessions_data=pd.read_csv('sessions.csv')
sessions_features=list(sessions_data.columns.values)

test_users_data=pd.read_csv('test_users.csv')
test_users_features=list(test_users_data.columns.values)

all_features_list=set().union(train_users_features,age_gender_features,countries_features,sessions_features,test_users_features)

### If you want to verify if there are NaN values for a feature in a dataset, use the following syntax:
## sp.sum(sp.isnan(train_users_data.age))

## Fill in the missing values

train_users_data.ix[train_users_data.age.isnull(),'age']=np.median(train_users_data[train_users_data.age.notnull()].age)

train_users_data.ix[train_users_data.date_first_booking.isnull(),'date_first_booking']=stats.mode(train_users_data[train_users_data.date_first_booking.notnull()].date_first_booking).mode[0]

# Split first_activity_time as date time and make new features

train_users_data['time_first_active']=pd.to_datetime(train_users_data.timestamp_first_active//1000000, format='%Y%m%d')
train_users_data['day']=train_users_data.timestamp_first_active//1000000 - (train_users_data.timestamp_first_active//100000000)*100
train_users_data['part_of_month']=pd.cut(train_users_data.day, 3, labels=["Start of month", "Mid month","End of month"])

train_users_data['first_affiliate_tracked']=train_users_data['first_affiliate_tracked'].replace(np.nan,'unknown')


train_users_data=pd.merge(left=train_users_data,right=countries_data, left_on='country_destination', right_on='country_destination')

sLength=len(train_users_data['age'])
train_users_data['age_bucket'] = pd.Series(np.empty(sLength, dtype=object), index=train_users_data.index)
encodeage()
train_users_data_copy=copy.deepcopy(train_users_data)
add_values_agb()
formatgender()

train_users_data['age_gender_dest']=train_users_data[['country_destination','gender','age_bucket']].apply(lambda x : '{}_{}_{}'.format(x[0],x[1],x[2]), axis=1)
age_gender_map['age_gender_dest']=age_gender_map[['country_destination','gender','age_bucket']].apply(lambda x : '{}_{}_{}'.format(x[0],x[1],x[2]), axis=1)

del_duplicate_columns()

train_users_data=pd.merge(left=train_users_data,right=age_gender_map, left_on='age_gender_dest', right_on='age_gender_dest')

ohe_features = ['gender','first_affiliate_tracked']
for f in ohe_features:
    train_users_data_dummy = pd.get_dummies(train_users_data[f], prefix=f)
    train_users_data = train_users_data.drop([f], axis=1)
    train_users_data = pd.concat((train_users_data, train_users_data_dummy), axis=1)

train_users_data_new.to_csv('train_users_v2.csv')