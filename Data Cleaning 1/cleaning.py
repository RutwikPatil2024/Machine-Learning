import pandas as pd
import numpy as np
df=pd.read_csv("data.csv")
print(df)
# print(df.info())
# print(df.head(10))
# print(df.tail(10))
# removing empty row
# print()
# newdf1=df.dropna(axis=0)
# print()
# replace empty row
# newdf2=df.replace(np.nan,375)
# newdf2=df.replace(np.nan,375)
# print(newdf2.loc[17])
# newdf=df.loc[:,"Calories"].replace(np.nan,375)
# print(df["Calories"])
newdf=df["Calories"].replace(np.nan,375)
print(newdf)
print()
print(newdf[17])

