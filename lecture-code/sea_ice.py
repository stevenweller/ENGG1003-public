import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sco

# dataset: September sea-ice extent 1979-2021
# https://climate.nasa.gov/vital-signs/arctic-sea-ice/
mydata = pd.read_csv("2485_Sept_Arctic_extent_1979-2021.csv")

year = mydata['year'].values
extent = mydata['extent'].values


def line(t, m, b):
    return m * t + b


# STRAIGHT-LINE FIT
popt, _ = sco.curve_fit(line, year, extent)
m = popt[0]
b = popt[1]

yearto2080 = range(1979, 2080)

print('extent(yr) = {:.3f}*yr + {:.3f}'.format(m, b))
print('Estimate September sea-ice extent is 0 in year = {}'.format(int(-b/m)))
plt.plot(year, extent, 'o')
plt.plot(yearto2080, line(yearto2080, m, b), 'r')
plt.plot(-b/m, 0, 'gs')   # green square when ice extent is zero
plt.xlabel('Year')
plt.ylabel('September sea-ice extent (million sq km)')
plt.grid()
plt.show()