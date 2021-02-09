# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
df = pd.read_excel('C:/Users/LENOVO/Desktop/ds/tablea-BI/data set/dsf.xlsx')
print(df)
sns.barplot(x=df['test'], y=df['int'])

df['expierence'].fillna(0,inplace=True)
df['test'].fillna(df['test'].mean(), inplace=True)
print(df)

cat = {'two':2, 'three':3, 'five':5, 'seven':7, 'eight':8, 'ten':10,0:0}
df['expierence'] = [cat[x] for x in df['expierence']]

print(df)

df['int'].fillna(df['int'].mean(), inplace=True)

print(df)

x=df.iloc[:,1:4]
print(x)

y=df['salary']
print(y)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x,y)

pickle.dump(reg, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))




















