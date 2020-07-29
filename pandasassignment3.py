# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:53:39 2020

@author: Prakash K
"""

import pandas as pd


flights=pd.read_csv("pandasdatasets/FlightDelays.csv")
##count of delayed flights
print(flights[(flights['Flight Status']=='delayed') & (flights['DAY_WEEK']>0) & (flights['DAY_WEEK']<6)].shape[0])
print(flights.dtypes)

##Averagedistance For Delayed Flights
print(flights[(flights['Flight Status']=='delayed') & (flights['DAY_WEEK']==5)].DISTANCE.mean())

##TotalDistance For Delayed flights
print(flights[(flights['Flight Status']=='delayed')& (flights['DAY_WEEK']==5)].DISTANCE.sum())

##Count Delayed flights
print(flights[(flights['Flight Status']=='delayed')& (flights['DAY_WEEK']==5)].DISTANCE.count())

##Ontime flights on Weekdays
print(flights[(flights['Flight Status']=='ontime')& (flights['DAY_WEEK']>0) & (flights['DAY_WEEK']<6)].shape[0])

##Ontime flights on Weekends
print(flights[(flights['Flight Status']=='ontime')& (flights['DAY_WEEK']==6) | (flights['DAY_WEEK']==0)].shape[0])

##number of Flights per destination
weekdayflights=flights[(flights['Flight Status']=='delayed') & (flights['DAY_WEEK']>0) & (flights['DAY_WEEK']<6)]
print(weekdayflights.groupby('DEST')['DAY_WEEK'].count())

##Weather was bad on weekdays
print(weekdayflights[weekdayflights.Weather==0 &  (flights['DAY_WEEK']>0) & (flights['DAY_WEEK']<6)].shape[0])

##Convert to dateformat
"""
flights.FL_DATE=pd.to_datetime(flights.FL_DATE)
print(flights.dtypes)
"""
##Convert to dateformat with Validation
from dateutil.parser import parse
print(flights.dtypes)
def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
for col in flights.columns:
                if flights[col].dtype=='object':
                    flights[col]=flights[col].transform(lambda x:pd.to_datetime(x) if is_date(x,True) else x)



