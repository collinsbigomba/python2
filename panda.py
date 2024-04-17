import pandas as pd

# data = pd.ExcelFile('crime_2015.xlsx')
# data = pd.read_excel(exc)

data = pd.read_excel('Crime_2015.xlsx')
# data = pd.read_excel('Crime_2015.xlsx')

# print(data.to_string(index=False))  # removes the 0  at the beginning and prints all columns
dat = data.to_string(index=False)

print(dat)
#print(dat.head())  # default is 5
