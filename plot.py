import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("area.csv")
x=df.area
y=df.prices
plt.plot(x,y,color='red',marker='*')
plt.show()
