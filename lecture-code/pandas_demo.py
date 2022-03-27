import pandas as pd

# read data from CSV file
mydata = pd.read_csv("tiny.csv")

# display first few rows
print(mydata.head())    # n=5 by default

# extract columns with username and student ID
username = mydata['Username'].values
ID = mydata['Student Identifier'].values