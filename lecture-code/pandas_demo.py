import pandas as pd

# read data from CSV file & display first few rows
mydata = pd.read_csv("tiny.csv")
print(mydata.head())

# extract columns with username and student ID
username = mydata['Username'].values
ID = mydata['Student Identifier'].values