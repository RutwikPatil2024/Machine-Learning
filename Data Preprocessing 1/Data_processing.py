import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import *

# reading csv
ds=pd.read_csv("Data.csv")
# ----------------------------------------------------------
# converting object to float of age column
# ds.columns=ds.columns.str.strip()
# ds["Age"]=pd.to_numeric(ds["Age"].str.strip(),errors="coerce")
# ds.to_csv("Data.csv",index=False)
# age(object) converted to age(float)
# --------------------------------------------------------------
#finding mean of age column and replacing it
# mean_age=ds["Age"].mean()
# ds["Age"].fillna(mean_age,inplace=True) inplace=True is depricated
# ds["Age"]=ds["Age"].replace(np.nan,mean_age)
# ds.to_csv("Data.csv",index=False)
# print(ds)
# print(mean_age)
# ------------------------------------------------------------------
# Converting salary object to float
# ds["Salary"]=pd.to_numeric(ds["Salary"].str.strip(),errors="coerce")
# ds.to_csv("Data.csv",index=False)
# print(ds.info())
# ------------------------------------------------------------------
# finding mean of salary and replacing it
# mean_salary=ds["Salary"].mean() 
# print(mean_salary)
# ds["Salary"]=ds["Salary"].replace(np.nan,mean_salary)
# ds.to_csv("Data.csv",index=False)
# ------------------------------------------------------------------
# Encoding Categorical variable
# value we predict is dependent variable  y
# value we consider is independent variable x
X=ds.iloc[:,0:3].values
# print(X)
y=ds.iloc[:,3:].values
# print(y)
# ------------------------------------------------------------------
# Scikit learn to replace a nan values 
# taking care of missing data using SimpleImputer 
# from sklearn.impute import SimpleImputer
# imp=SimpleImputer(missing_values=np.nan,strategy="mean")
# imp.fit(X[:,1:3])
# X[:,1:3]=imp.transform(X[:,1:3])
# -------------------------------------------------------------------