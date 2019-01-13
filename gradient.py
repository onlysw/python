import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def gradient_descent(x,y):
    m_curr = b_curr = 0
    rate = 0.01
    n = len(x)
    plt.scatter(x,y,color='red',marker='+',linewidth='5')
    plt.xlabel('area')
    plt.ylabel('prices')
    for i in range(10):
        y_predicted = m_curr * x + b_curr
#         print (m_curr,b_curr, i)

        plt.plot(x,y_predicted,color='green')

        md = -(2/n)*sum(x*(y-y_predicted))
        yd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - rate * md
        b_curr = b_curr - rate * yd
df=pd.read_csv("area.csv")
#print(df)
x=df.area
y=df.prices


gradient_descent(x,y)
plt.show()
