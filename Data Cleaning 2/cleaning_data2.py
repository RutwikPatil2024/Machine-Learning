import pandas as pd
import numpy as np

df=pd.read_csv("cleaning_data.csv")
# print(df)
# cal=df["Calories"].mean()
# print(cal)
# df.fillna(cal,inplace=True)
# df.to_csv("cleaning_data.csv",index=False)
# --------------------------------------------
# print(df.loc[25])
# df.drop(25,inplace=True)
# df.to_csv("cleaning_data.csv",index=False)
# -----------------------------------------------
df["Date"]=pd.to_datetime(df["Date"])
df.to_csv("cleaning_data.csv",index=False)
# print(df.to_string())
print(df)