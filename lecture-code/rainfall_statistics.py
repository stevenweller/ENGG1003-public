import pandas as pd

# read rainfall data from spreadsheet
rainfallData = pd.read_csv("Rainfall.csv")
print(rainfallData.head())

# extract columns for years 2010 and 2020
rainfall2010 = rainfallData['Rainfall 2010'].values
rainfall2020 = rainfallData['Rainfall 2020'].values

N = len(rainfall2010)       # total number of regions

# count regions where rainfall has decreased from 2010 to 2020
decCount = 0
for i in range(0, N):
    if rainfall2020[i] < rainfall2010[i]:
        decCount += 1

decPercent = 100 * decCount/N
print('{} out of {} regions have reduced rainfall, which is {:5.2f}%'
      .format(decCount, N, decPercent))