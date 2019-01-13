import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('homeprices.csv')

import math
med_bedrooms = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(med_bedrooms)
print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

print("regration coefficcient:=",reg.coef_)
print("regression intersept",reg.intercept_)
print("predicted value for area 3000 bed 3 and age 40 ",reg.predict([[3000, 3, 40]]))
