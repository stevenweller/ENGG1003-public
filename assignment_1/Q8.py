import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

# -------------------------------------------------------------------
# Q8(a)
mydata = pd.read_csv("rainfall-1.csv")

rainfall = mydata['Monthly Precipitation Total (millimetres)'].values
year = mydata['Year'].values
month = mydata['Month'].values

# calendar.month_abbr[] is a built-in array in the calendar module
# calendar.month_abbr[1] == Jan, calendar.month_abbr[2] == Feb, ..., calendar.month_abbr[12] == Dec
# https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python
print("First month & year = {} {}".format(calendar.month_abbr[month[0]], year[0]))
# month[-1] is the final entry in month array, ie: month[len(month)-1], similarly for year[-1]
print("Last month & year  = {} {}".format(calendar.month_abbr[month[-1]], year[-1]))

num_months = len(rainfall)
num_yrs = year[-1] - year[0] + 1

print("Number of months = {}".format(num_months))
print("Number of years = {}\n\n".format(num_yrs))

# Calculate statistics on data ------------------------------------------------
# Jan (m=0), Feb (m=1), ..., Dec (m=11)

avg = np.zeros(12)
minrain = np.zeros(12)
maxrain = np.zeros(12)

# for each month m=0 (Jan),m=1 (Feb),...,m=11 (Dec)
for m in range(0, 12):
    total = 0
    minrain[m] = 1_000_000
    maxrain[m] = 0
    # pick out rainfall in specified month
    # m=0 (Jan): i=0,12,24,36,...
    # m=1 (Feb): i=1,13,25,37,...
    # ...
    # m=11 (Dec): i=11,23,35,...
    for i in range(m, num_months, 12):
        total += rainfall[i]

        if rainfall[i] < minrain[m]:
            minrain[m] = rainfall[i]

        if rainfall[i] > maxrain[m]:
            maxrain[m] = rainfall[i]

    avg[m] = total/num_yrs

    print("Average {} rainfall: {:.2f} mm".format(calendar.month_abbr[month[m]], avg[m]))
    print("Minimum {} rainfall: {:.2f} mm".format(calendar.month_abbr[month[m]], minrain[m]))
    print("Maximum {} rainfall: {:.2f} mm\n".format(calendar.month_abbr[month[m]], maxrain[m]))

# -------------------------------------------------------------------
# Q8(b)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(months, avg)
plt.title("Location: 061055 Newcastle Nobbys Signal Station")
plt.xlabel("Month")
plt.ylabel("Mean rainfall (mm) over 1867-1998")
plt.show()
