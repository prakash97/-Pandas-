
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("pandasdatasets/outcome-of-care-measures.csv")
df['Hospital 30-Day Death Mortality Rates from Heart Attack']= pd.to_numeric(df['Hospital 30-Day Death Mortality Rates from Heart Attack'].replace('Not Available',np.nan))
df_mean=df['Hospital 30-Day Death Mortality Rates from Heart Attack'].mean()
df['Hospital 30-Day Death Mortality Rates from Heart Attack']=df['Hospital 30-Day Death Mortality Rates from Heart Attack'].apply(lambda x:df_mean if np.isnan(x) else x)
df['Hospital 30-Day Death (Mortality) Rates from Heart Failure']= pd.to_numeric(df['Hospital 30-Day Death (Mortality) Rates from Heart Failure'].replace('Not Available',np.nan))
df_mean=df['Hospital 30-Day Death (Mortality) Rates from Heart Failure'].mean()
df['Hospital 30-Day Death (Mortality) Rates from Heart Failure']=df['Hospital 30-Day Death (Mortality) Rates from Heart Failure'].apply(lambda x:df_mean if np.isnan(x) else x)
df['Hospital 30-Day Death (Mortality) Rates from Pneumonia']= pd.to_numeric(df['Hospital 30-Day Death (Mortality) Rates from Pneumonia'].replace('Not Available',np.nan))
df_mean=df['Hospital 30-Day Death (Mortality) Rates from Pneumonia'].mean()
df['Hospital 30-Day Death (Mortality) Rates from Pneumonia']=df['Hospital 30-Day Death (Mortality) Rates from Pneumonia'].apply(lambda x:df_mean if np.isnan(x) else x)
"""
plt.plot(df['Provider Number'],df['Hospital 30-Day Death Mortality Rates from Heart Attack'])
plt.xlabel("Provider Number")
plt.ylabel("Heart Attack Mortality Rate")
plt.show()
"""
#print(df)

##Best Hospital statewise
df['Statewise Combined Moratlity Rate']=df['Hospital 30-Day Death (Mortality) Rates from Heart Failure']+df['Hospital 30-Day Death (Mortality) Rates from Heart Failure']+df['Hospital 30-Day Death (Mortality) Rates from Pneumonia']
best_state_groupwise=df.groupby('State').apply(lambda x: x.sort_values(['Statewise Combined Moratlity Rate'], ascending = True))
print(best_state_groupwise)
print(best_state_groupwise.groupby('State').head(1)['Hospital Name'])

##Ranking hospital statewise
df["Rank_state_wise"] = df.groupby('State')['Statewise Combined Moratlity Rate'].rank("dense", ascending=True)
print(df['Rank_state_wise'])

##Ranking hospital by all states
df["Rank"] = df['Statewise Combined Moratlity Rate'].rank(method='min')
print(df['Rank'])