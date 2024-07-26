import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds=pd.read_csv("Data.csv")
# print(ds.info())

X=ds.iloc[:,0:1].values
y=ds.iloc[:,1:].values
# print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=0)

# plt.scatter(X,y)
# plt.show()

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)

# print(reg.coef_)
# print(reg.intercept_)
# y=ax + b
# result=9377.71581254 * 1.1 + 26562.39929261
# print(result)

plt.scatter(X,y)
plt.plot(X,reg.predict(X))
# plt.show()

result=reg.predict([[12]])
print(result)