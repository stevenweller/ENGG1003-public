import pandas as pd

# read data from  & display first few rows
mydata = pd.read_csv("tiny.csv")
print(mydata.head())

# extract columns with username and student ID
username = mydata['Username'].values
ID = mydata['Student Identifier'].values

# display username and ID data
print(username)
print(ID)