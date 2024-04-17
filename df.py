import pandas as pd

df = pd.read_excel('Crime_2015.xlsx')

print(df)
print(df.shape)
print(df.columns)
print(df.CITY)

print(df.iloc(1))
