import pandas as pd
import numpy as np
df=pd.read_excel("C:\programming\python\\numpy\project\\numpy_example.xlsx")
df["Bonus"]=df["Bonus"].interpolate(method="linear")
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df["Rating"].fillna(df["Rating"].median(),inplace=True)
df.drop_duplicates(subset="EmployeeID",keep="first",inplace=True)
df.loc[9,"Salary"]=-14523
df["Salary"]=np.where(df["Salary"]<0,df["Salary"].mean(),df["Salary"])
print(df)
