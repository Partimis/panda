import pandas as pd
import numpy as np
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-D'
                 'A0101EN-SkillsNetwork/labs/Data%20files/auto.csv', header=None)
header = ["id", "name", "price", "id", "name", "value", "id", "name", "value","id", "name", "value","id", "name", "value", "id", "name", "value", "id", "name", "value","id", "name", "value","yekimande","akhar"]
df.columns = header
df1 = df.replace('?', np.NaN)
df = df1.dropna(subset = ['price'] , axis = 0)
print(df1.dtypes)
print(df1.describe(include = "all"))
print(df1.info())
