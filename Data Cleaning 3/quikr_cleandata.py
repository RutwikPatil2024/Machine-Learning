import numpy as np
import pandas as pd
df=pd.read_csv("quikr_car.csv")
# df.drop(195,inplace=True)
# print(df.loc[195])
# if 195 in df.index:
#     print(df.loc[195])
# else:
#     print("195 is deleted")
# -----------------------------------------
# print(df.loc[182])
# df.drop(185,inplace=True)
# if 185 in df.index:
#     print(df.loc[185])
# else:
#     print("185 is deleted")
# for x in df.index:
#     print(df.loc[x,"year"])
# df.to_csv("quikr_car.csv",index=False)
# df.drop(200,inplace=True)
# -------------------------------------------
# print(df.iloc[287])
# df.drop(287,inplace=True)
# -------------------------------------------
# print(df.iloc[279])
# df.drop(287,inplace=True)
# df.to_csv("quikr_car.csv",index=False)
# if 279 in df.index:
#     print(df.loc[279])
# else:
#     print("279 is deleted")
# print(df.index)
# print(df.loc[279])
# --------------------------------------------------------------------
# index_to_drop = df.index[[370,380,386,399,417,418,426,545,578,584,593]] 
# print(df.loc[index_to_drop])
# df.drop(index_to_drop,inplace=True)
# df.to_csv("quikr_car.csv",index=False)
# ---------------------------------------------------------------------
# index_to_drop = df.index[[588,590,598,609,617,619,697,699,702,732,738]] 
# print(df.loc[index_to_drop])
# df.drop(index_to_drop,inplace=True)
# df.to_csv("quikr_car.csv",index=False)
# ----------------------------------------------------------------------
# index_to_drop = df.index[[746,747,780,819,822]] 
# # print(df.loc[index_to_drop])
# df.drop(index_to_drop,inplace=True)
# df.to_csv("quikr_car.csv",index=False)
# ----------------------------------------------------------------------
# changing dataype of year
# year=df.iloc[:,2:3]
# print(type(year))
# year = year.astype(int)
# df[2]=year
# df.to_csv("quikr_car.csv",index=False)
# print(df.info())
# -------------------------------------------------------------------------
# Ask For Price 
# droplist=[]
# for x in df.index:
#     if df.iloc[x,3]=="Ask For Price ":
#         droplist.append(x)
#         # print(x)

# print(droplist)       
# df.drop(droplist,inplace=True)       
# df.to_csv("quikr_car.csv",index=False)
# ------------------------------------------------------------------------
# converting price to int
# price = df.iloc[:, 3]
# price_cleaned = price.str.replace(',', '')
# cleaned=price_cleaned.astype(int)
# for x in range(len(cleaned)):
#     df.iloc[x:,3]=cleaned[x]
# df.to_csv("quikr_car.csv",index=False)
# print(df.head(10))
# ------------------------------------------------------------------------
# fuel_type cleaning 
# df.dropna(inplace=True)
# df.to_csv("quikr_car.csv",index=False)
# ------------------------------------------------------------------------
# converting kms colum in int
# dist = df.iloc[:,4]
# dist_clean = dist.str.replace(',', '')
# rmkms=dist_clean.str.replace('kms','')
# rmkms=rmkms.astype(int)
# print(rmkms)
# for x in range(len(rmkms)):
#     df.iloc[x:,4]=rmkms[x]
# df.to_csv("quikr_car.csv",index=False)
# for x in range(len(rmkms)):
#     df.iloc[x:,4]=rmkms[x]
# ------------------------------------------------------------------------
# droping row which have running less than 1000 (kms_driven)
# for x in range(len(df.iloc[:,4])):
#     if df.iloc[x:,4]<1000:
#         print(x)
# -----------------------------------------------------------------------
# removing trailing and leading spaces
# df.columns = df.columns.str.strip()
# df.to_csv("quikr_car.csv",index=False)
# ----------------------------------------------------------------------
# converting company name to string
# print(df.info())
# company = df.iloc[:,1]
# company=company.astype(str)
# company=company.str.strip()
# # print(company)
# print(type(company[0]))
# for x in range(len(company)):
#     df.iloc[x:,1]=company[x]
# df.to_csv("quikr_car.csv",index=False)
# # print(df.info())
# ------------------------------------------------------------------------
# Duplicate rows
dupli=df.duplicated()
# for x in range(len(dupli)):
#     print(dupli[x])
df.drop_duplicates(inplace=True)
df.to_csv("quikr_car.csv",index=False)
print(df.info())