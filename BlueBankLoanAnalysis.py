# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:45:58 2024

@author: dilas
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file=open ('loan_data_json.json')
data=json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data=json.load(json_file)
    
#transform to data frame
loandata=pd.DataFrame(data)

#finding unique values for the purpose column

loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using EXP() to get the annual income from log annual inc field 
income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income

#working with arrays

#1D array
arr=np.array([1,2,3,4])

#0D array
arr=np.array(43)

#2D array
arr=np.array([[1,2,3],[4,5,6]])

#working with IF statements
a=40
b=500
if b>a:
    print('b is greater than a')
    
#Lets add more conditions
a=40
b=500
c=1000
if b>a and b<c:
    print('b is greater than a but less than a')

#what if condition is not met?
a=40
b=500
c=20

if b>a and b<c:
    print('b is greater than a but less than a')
else:
    print('No conditions met')
    
#another condition different metrics
a=40
b=0
c=30
if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print("b is greater than a and c")
else:
    print('no conditions met')
    
#using or statement
a=40
b=500
c=30
if b>a or b<c:
    print('b is greater than a or less than c')
else:
    print('no conditions met')
    
#fico scores
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

fico=250
if fico>=300 and fico<400:
    ficocat='Very Poor'
elif fico>=400 and fico<600:
    ficocat='Poor'
elif fico>=601 and fico<660:
    ficocat='Fair'
elif fico>=660 and fico<780:
    ficocat='Good'
elif fico>=780:
    ficocat='Excellent'
else:
    ficocat='Unknown'
print(ficocat)

#working with for loops
fruits= ['apple','pear','banana','cherry']
for x in fruits:
    print(x)
    y=x+ ' fruit'
    print(y)

for x in range(0,4):
    y=fruits[x]+ ' for sale'
    print(y)

#applying for loops to loan data
#using first 10 data lines
length=len(loandata)
ficocat=[]
for x in range (0, length):
    category=loandata['fico'][x]
    
    try:
        if category>=300 and category<400:
            cat='Very Poor'
        elif category>=400 and category<600:
            cat='Poor'
        elif category>=601 and category<660:
            cat='Fair'
        elif category>=660 and category<700:
            cat='Good'
        elif category>=700:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
            cat='Unknown'
    ficocat.append(cat)

ficocat=pd.Series(ficocat)

loandata['fico.category']=ficocat

#whileloops
i=1
while i<10:
    print (i)
    i=i+1

#df.loc as conditional statements
#df.loc(df[columnname]condition, newcolumnname)='value if the condition is met'

#for interest rates, a new column is wanted if the rate >0.12 then high, else low
loandata.loc[loandata['int.rate']>0.12, 'intrate.type']='High'
loandata.loc[loandata['int.rate']<=0.12, 'intrate.type']='Low'   

#number of loans/rows by FICO category, size represents the number of rows
catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width=0.5)
plt.show()
purposeplot=loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color='red',width=0.3)
plt.show()

#scatter plots higher your income, the less dti lower debt
ypoint=loandata['annualincome']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint, color='#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)
