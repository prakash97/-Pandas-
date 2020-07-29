# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 01:50:41 2020

@author: Prakash K
"""
###Assignment3
import pandas as pd

flights=pd.read_csv("pandasdatasets/FlightDelays.csv")
##count of delayed flights
print(flights[(flights['Flight Status']=='delayed') & (flights['DAY_WEEK']>0) & (flights['DAY_WEEK']<6)].shape[0])



##Assignement4
##datatypes & dimension
airfares=pd.read_csv("pandasdatasets/Airfares.csv")
print(airfares.dtypes)
print(airfares.shape)


##missing data & max data to be lost
print(airfares.applymap(lambda x: x=='*').sum())
print(airfares.applymap(lambda x: x=='*').sum().sum())
print(airfares.applymap(lambda x: x=='*').sum().max())

##cleaning the data

for col in airfares.columns:
  if airfares[col].dtype=='object':
      airfares[col]=airfares[col].str.replace('*','Missing')
print(airfares)
for col in airfares.columns:
  if airfares[col].dtype=='object':
      airfares[col]=airfares[col].apply(lambda x:x.replace('$','') if '$' in x else x)

airfares['FARE']=airfares.FARE.astype(float)
print(airfares.FARE)


##Average fair for vacation
mean_airfares=airfares.groupby('VACATION')['FARE'].mean()
print(mean_airfares)

##split city and state column names
airfares['S_STATE']=airfares['S_CITY'].str.split(' ').str[-1]
airfares['S_CITI']=airfares['S_CITY'].str.split(' ').str[0]+airfares['S_CITY'].str.split(' ').str[1]
print(airfares['S_STATE'],airfares['S_CITI'])
airfares['E_STATE']=airfares['E_CITY'].str.split(' ').str[-1]
airfares['E_CITI']=airfares['E_CITY'].str.split(' ').str[0]+airfares['E_CITY'].str.split(' ').str[1]
print(airfares['E_STATE'],airfares['E_CITI'])


##Average fair for free or controlled
mean_airfares=airfares.groupby('SLOT')['FARE'].mean()
print(mean_airfares['Controlled']-mean_airfares['Free'])

##Average fair for free or constrained
mean_airfares=airfares.groupby('GATE')['FARE'].mean()
print(mean_airfares['Constrained']-mean_airfares['Free'])

##binning the data

airfares['S_INCOME']=airfares['S_INCOME'].str.replace(',','')
airfares['S_INCOME']=airfares['S_INCOME'].astype(float)
#print(airfares['S_INCOME'].dtype)
airfares['BIN_S_INCOME']=pd.cut(airfares['S_INCOME'],bins=[20000,22000,24000,26000,28000,30000,32000,34000,36000,38000,40000],
        labels=['20000-22000','22000-24000','24000-26000','26000-28000','28000-30000','30000-32000','32000-34000',
               '34000-36000','36000-38000','38000-40000'])
print(airfares['BIN_S_INCOME'])


airfares['E_INCOME']=airfares['E_INCOME'].str.replace(',','')
airfares['E_INCOME']=airfares['E_INCOME'].astype(float)
#print(airfares['E_INCOME'].dtype)
airfares['BIN_E_INCOME']=pd.cut(airfares['E_INCOME'],bins=[20000,22000,24000,26000,28000,30000,32000,34000,36000,38000,40000],
        labels=['20000-22000','22000-24000','24000-26000','26000-28000','28000-30000','30000-32000','32000-34000',
               '34000-36000','36000-38000','38000-40000'])
print(airfares['BIN_E_INCOME'])


##Bin all numeric datas

airfares['BIN_COUPON']=pd.cut(airfares['COUPON'],bins=[0,0.5,1],
        labels=['0-0.5','0.5-1'])
print(airfares['BIN_COUPON'])

airfares['BIN_NEW']=pd.cut(airfares['NEW'],bins=[0,1,2,3],
        labels=['0-1','1-2','2-3'])
print(airfares['BIN_NEW'])

airfares['BIN_HI']=pd.cut(airfares['HI'],bins=[1000,3000,5000,7000,9000],
        labels=['1000-3000','3000-5000','5000-7000','7000-9000'])
print(airfares['BIN_HI'])

airfares['BIN_SPOP']=pd.cut(airfares['S_POP'],bins=[1000000,3000000,5000000,7000000,9000000],
        labels=['1000000-3000000','3000000-5000000','5000000-7000000','7000000-9000000'])
print(airfares['BIN_SPOP'])

airfares['BIN_EPOP']=pd.cut(airfares['E_POP'],bins=[1000000,3000000,5000000,7000000,9000000],
        labels=['1000000-3000000','3000000-5000000','5000000-7000000','7000000-9000000'])
print(airfares['BIN_EPOP'])


airfares['BIN_DISTANCE']=pd.cut(airfares['DISTANCE'],bins=[100,500,1000,1500,2000,2500,3000],
        labels=['100-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000'])
print(airfares['BIN_DISTANCE'])

airfares['BIN_PAX']=pd.cut(airfares['PAX'],bins=[1000,5000,10000,15000,20000],
        labels=['1000-5000','5000-10000','10000-15000','15000-20000'])
print(airfares['BIN_PAX'])

airfares['BIN_FARE']=pd.cut(airfares['FARE'],bins=[10,50,100,150,200],
        labels=['10-50','50-100','100-150','150-200'])
print(airfares['BIN_FARE'])

airfares['BIN_EPOP']=pd.cut(airfares['E_POP'],bins=[1000000,3000000,5000000,7000000,9000000],
        labels=['1000000-3000000','3000000-5000000','5000000-7000000','7000000-9000000'])
print(airfares['BIN_EPOP'])

print(airfares.dtypes)

##Outliers
COUPON_IQR=airfares.COUPON.describe()['75%']-airfares.COUPON.describe()['25%']
COUPON_LB=airfares.COUPON.describe()['25%']+1.5*(COUPON_IQR)
COUPON_UB=airfares.COUPON.describe()['75%']+1.5*(COUPON_IQR)
print(airfares[(airfares.COUPON<COUPON_LB) & (airfares.COUPON>COUPON_UB)].COUPON)

NEW_IQR=airfares.NEW.describe()['75%']-airfares.NEW.describe()['25%']
NEW_LB=airfares.NEW.describe()['25%']+1.5*(NEW_IQR)
NEW_UB=airfares.NEW.describe()['75%']+1.5*(NEW_IQR)
print(airfares[(airfares.NEW<NEW_LB) & (airfares.NEW>NEW_UB)].NEW)

HI_IQR=airfares.HI.describe()['75%']-airfares.HI.describe()['25%']
HI_LB=airfares.HI.describe()['25%']+1.5*(HI_IQR)
HI_UB=airfares.HI.describe()['75%']+1.5*(HI_IQR)
print(airfares[(airfares.HI<HI_LB) & (airfares.HI>HI_UB)].HI)

SINCOME_IQR=airfares.S_INCOME.describe()['75%']-airfares.S_INCOME.describe()['25%']
SINCOME_LB=airfares.S_INCOME.describe()['25%']+1.5*(SINCOME_IQR)
SINCOME_UB=airfares.S_INCOME.describe()['75%']+1.5*(SINCOME_IQR)
print(airfares[(airfares.S_INCOME<SINCOME_LB) & (airfares.S_INCOME>SINCOME_UB)].S_INCOME)

SINCOME_IQR=airfares.E_INCOME.describe()['75%']-airfares.E_INCOME.describe()['25%']
SINCOME_LB=airfares.E_INCOME.describe()['25%']+1.5*(SINCOME_IQR)
SINCOME_UB=airfares.E_INCOME.describe()['75%']+1.5*(SINCOME_IQR)
print(airfares[(airfares.E_INCOME<SINCOME_LB) & (airfares.E_INCOME>SINCOME_UB)].E_INCOME)


DISTANCE_IQR=airfares.DISTANCE.describe()['75%']-airfares.DISTANCE.describe()['25%']
DISTANCE_LB=airfares.DISTANCE.describe()['25%']+1.5*(DISTANCE_IQR)
DISTANCE_UB=airfares.DISTANCE.describe()['75%']+1.5*(DISTANCE_IQR)
print(airfares[(airfares.DISTANCE<DISTANCE_LB) & (airfares.DISTANCE>DISTANCE_UB)].DISTANCE)

FARE_IQR=airfares.FARE.describe()['75%']-airfares.FARE.describe()['25%']
FARE_LB=airfares.FARE.describe()['25%']+1.5*(FARE_IQR)
FARE_UB=airfares.FARE.describe()['75%']+1.5*(FARE_IQR)
print(airfares[(airfares.FARE<FARE_LB) & (airfares.FARE>FARE_UB)].FARE)

PAX_IQR=airfares.PAX.describe()['75%']-airfares.PAX.describe()['25%']
PAX_LB=airfares.PAX.describe()['25%']+1.5*(PAX_IQR)
PAX_UB=airfares.PAX.describe()['75%']+1.5*(PAX_IQR)
print(airfares[(airfares.PAX<PAX_LB) & (airfares.PAX>PAX_UB)].PAX)

##average fare based on starting or ending city
print(airfares.groupby('S_CITY')['FARE'].mean())
print(airfares.groupby('E_CITY')['FARE'].mean())
print(airfares.groupby(['S_CITY','E_CITY'])['FARE'].mean())
