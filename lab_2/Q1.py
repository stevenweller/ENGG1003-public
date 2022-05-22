import pandas as pd

mydata = pd.read_csv("tiny.csv")
lastname = mydata["Last name"].values
firstname = mydata["First name"].values
ID = mydata["Student Identifier"].values

print(lastname)

for i in range(0, len(ID)):
    if ID[i] < 5000:
        print(firstname[i])
