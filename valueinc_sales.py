# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:25:38 2024

@author: dilas
"""

import pandas as pd

#import data from a file called transactions.csv
#file_name=pd.read_csv('file.csv')

data=pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep=';')

#summary of the data table
data.info()

#playing around wiht variables

#working with calcualtions

#Ddefining variables

CostPerItem=11.73
SellingPricePerItem= 21.11
NumberofItemsPurchased =6

#Mathematical operations on Python

ProfitPerItem=21.11-11.73
ProfitPerItem=SellingPricePerItem - CostPerItem

ProfitPerTransaction= NumberofItemsPurchased * ProfitPerItem
CostPerTransaction= CostPerItem * NumberofItemsPurchased
SellingPricePerTransaction= SellingPricePerItem * NumberofItemsPurchased

#CostPerTranasction Column Calculation

#CostPerTransaction= CostPerItem * NumberofItemsPurchased

#variable= dataframe['column_name']

CostPerItem=data['CostPerItem']

NumberofItemsPurchased=data['NumberOfItemsPurchased']

CostPerTransaction= CostPerItem * NumberofItemsPurchased

#Adding a new column to a dataframe

data['CostPerTransaction']=CostPerTransaction

#Sales Per Transaction

data['SalesPerTransaction']=data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#Profit Calculation

data['ProfitPerTransaction']=data['SalesPerTransaction']- data['CostPerTransaction']

#Markeup = [Sales - Cost]/Cost

data['MarkUp']= data['ProfitPerTransaction']/ data['CostPerTransaction']

#Rounding Mark Up 

roundmarkup=round(data['MarkUp'],2)

data['MarkUp']=round(data['MarkUp'],2)

#Combining data fields

my_name='Dilasha'+ ' Dixit'

my_date='Day'+'-'+'Month'+'-'+'Year'

my_date= data['Day']+'-'

#checking columns data type

print(data['Day'].dtype)

#Change columns type

day= data['Day'].astype(str)
year=data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date= day+'-'+data['Month']+'-'+ year

data['date']=my_date

#using iloc to view specific columns or rows
data.iloc[0]

data.iloc[0:3]

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings all rows in the 2nd column

data.ilow[4,2] #brings in 4th row, 2nd column

#using split to delimit the client keywords field
#new_var=column.str.split('sep',expand=True)

split_col=data['ClientKeywords'].str.split(',',expand=True)

#creating new columns for the split columns in Client Keyword

data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]

#using replace function
data['ClientAge']=data['ClientAge'].str.replace('[','')

data['LengthofContract']=data['LengthofContract'].str.replace(']','')

data['ItemDescription']=data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new data set

seasons=pd.read_csv('value_inc_seasons.csv', sep=';')
#merge files: merge_df=pd.merge(df_old,df_new, on='key')

data=pd.merge(data,seasons,on='Month')

#dropping columns
#df=df.drop('columnname',axis=1)

data=data.drop('ClientKeywords', axis=1)
data=data.drop('Day',axis=1)

data=data.drop(['Year','Month'],axis=1)

#Export into a CSV
data.to_csv('ValueInc_Cleaned.csv', index=False)
