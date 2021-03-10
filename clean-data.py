import pandas as pd
import numpy as np
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-D'
                 'A0101EN-SkillsNetwork/labs/Data%20files/auto.csv', header=None)
header = ["id", "name", "price1", "id", "name", "value", "id", "name", "value","id", "name", "value","id", "name",
          "value", "id", "name", "value", "id", "name", "value","id", "name", "value","yekimande","price"]
df.columns = header
df1 = df.replace('?', np.NaN)
df1.dropna(subset=['price'], axis = 0, inplace=True)
df1['price'] = df1['price'].astype('float')
print(df1.dtypes)
print(df1.describe(include="all"))
print(df1.info())
print(df1.head(10))
df1['price'] = (df1['price']-df1['price'].mean())/df1['price'].std()
print(df1['price'])