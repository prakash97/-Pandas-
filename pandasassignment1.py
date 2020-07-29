##Pandas Assignment

##Assignment1
import datetime as dt
import numpy as np
import pandas as pd

train= pd.read_csv("pandasdatasets/ex1.csv")
print(train.LoanAmt.isnull().sum())
print('-------------------------------------')
##Assignment2

train= pd.read_csv("pandasdatasets/ex1.csv")
print(train[~train.Credit_History.isnull()])
print('-------------------------------------')
##Assignment3

train= pd.read_csv("pandasdatasets/ex1.csv")
print(train.
      na(axis=0,how='any',thresh=5))
print('-------------------------------------')
##Assignment4
train= pd.read_csv("pandasdatasets/ex21.csv")
print(train.Item_Fat_content.astype('category'))
print('-------------------------------------')
##assignment5
train= pd.read_csv("pandasdatasets/ex2.csv")
train_dict={'Urban':'City','SemiUrban':'City','Rural':'Village'}
train['PropertyArea']=train.PropertyArea.replace(train_dict)
#print(train.PropertyArea.apply(train_dict).astype(object))
print(train)
print('-------------------------------------')
##Assignment6
train= pd.read_csv("pandasdatasets/ex1.csv")
print(train[(train.Gender=='Male') & (train.Married=='Yes')].shape[0])
print(float(train.shape[0]))
print(train[(train.Gender=='Male') & (train.Married=='Yes')].shape[0]/(float(train.shape[0]))*100)
print('-------------------------------------')

##Assingment7
train=pd.read_csv("pandasdatasets/ex3.csv")
test=pd.read_csv("pandasdatasets/ex4.csv")
print(set(test.columns).difference(train.columns))
print('-------------------------------------')


##Assingment8
train=pd.read_csv("pandasdatasets/ex3.csv")
train['Gender']=train.Gender.map({'M':1,'F':0}).astype(int)
print(train.Gender)
print('-------------------------------------')


##Assignment9
train=pd.read_csv("pandasdatasets/ex6.csv")
test=pd.read_csv("pandasdatasets/ex7.csv")
print(set(test.Product_ID.unique()).issubset(train.Product_ID.unique()))
print('-------------------------------------')


##Assignment10
train=pd.read_csv("pandasdatasets/ex3.csv")
train['Age']=train.Age.apply(lambda x:np.array(x.split('-'),dtype=int).mean())
print(train.Age)
print('-------------------------------------')


##Assignment11
train=pd.read_csv("pandasdatasets/ex8.csv")
print(train.Ticket.str.split(" ").str[-1])
print('-------------------------------------')


##Assignment12
train=pd.read_csv("pandasdatasets/ex8.csv")
#print(train.Age,train.Sex)
print(train.groupby("Sex")['Age'].mean())
print(train.groupby("Sex")['Age'].transform(lambda x:x.fillna(x.mean())))
train['Age']=train.groupby("Sex")['Age'].transform(lambda x:x.fillna(x.mean()))
print(train.Age)
print('-------------------------------------')


##Assignment13
train=pd.read_csv("pandasdatasets/ex8.csv")
print(train.Cabin.isnull().astype(int))
print('-------------------------------------')


##Assignment14
train=pd.read_csv("pandasdatasets/ex9.csv",header=None,names=['1','2','3','4'])
print(train)
print('-------------------------------------')


##Assignement15
train=pd.read_csv("pandasdatasets/ex21.csv")
print(train.columns)
print(train.Item_Identifier.str.startswith('F'))
print('-------------------------------------')


##Assignement16
train=pd.read_csv("pandasdatasets/ex22.csv")
datetime=pd.to_datetime(train.Date_time_of_event)
print(datetime.dt.day)
print('-------------------------------------')

##Assignement17
train=pd.read_csv("pandasdatasets/ex22.csv")
datetime=pd.to_datetime(train.Date_time_of_event)
print(datetime.dt.weekday_name)
print('-------------------------------------')


##Assignement18
train=pd.read_csv("pandasdatasets/ex15.csv")
datetime=pd.to_datetime(train.TIMESTAMP)
print(datetime)
print('-------------------------------------')

##Assignement19
train=pd.read_csv("pandasdatasets/ex16.csv")
datetime1=pd.to_datetime(train.Date_time_of_event)
print(pd.datetime.now()-datetime1)
#print(datetime1)
print('-------------------------------------')

##Assignement20
train=pd.read_csv("pandasdatasets/ex13.csv")
train.Date_time_of_event=pd.to_datetime(train.Date_time_of_event)
train.Date_time_of_event=train.Date_time_of_event.apply(lambda x:x.replace(day=1))
print(train.Date_time_of_event)
#print(datetime1)
print('-------------------------------------')

##Assignement21
train=pd.read_csv("pandasdatasets/ex13.csv")
train.Date_time_of_event=pd.to_datetime(train.Date_time_of_event)
train.Date_time_of_event=train.Date_time_of_event.apply(lambda x:x.replace(day=1))
print(train.Date_time_of_event)
#print(datetime1)
print('-------------------------------------')


##Assignement22
train=pd.read_csv("pandasdatasets/ex20.csv")
print(train.dtypes)
print(train.cumsum(axis=0))
#print(datetime1)
print('-------------------------------------')

##Assignement23
train=pd.read_csv("pandasdatasets/ex17.csv")
student=pd.read_csv("pandasdatasets/ex18.csv")
internship=pd.read_csv("pandasdatasets/ex19.csv")
print(train.columns)
#print(student.columns)
#print(internship.columns)
train=pd.merge(train,internship,on='Internship_ID',how='inner')
train=pd.merge(train,student,on='Student_ID',how='inner')
print(train)
print('-------------------------------------')

##Assingment24
student=pd.read_csv("pandasdatasets/ex18.csv")
student.drop_duplicates(subset=['Student_ID'],keep='first',inplace=False)
print(student)
print('-------------------------------------')

##Assingment25
train=pd.read_csv("pandasdatasets/ex20.csv")
print(train.columns)
#train.drop("sleep")
print(train)
print('-------------------------------------')