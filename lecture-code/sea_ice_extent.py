# sea_ice_extent
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def line(x, m, b):
    return m * x + b

# dataset: September sea-ice extent 1979-2020
# https://climate.nasa.gov/vital-signs/arctic-sea-ice/
year = np.arange(1979, 2021)
extent = np.array([7.05,7.67,7.14,7.3,7.39,6.81,6.7,7.41,
        7.28,7.37,7.01,6.14, 6.47,7.47,6.4,7.14,6.08,
        7.58,6.69,6.54,6.12,6.25,6.73,5.83,6.12,
        5.98,5.5,5.86,4.27,4.69,5.26,4.87,4.56,
        3.57,5.21,5.22,4.62,4.53,4.82,4.79,4.36,3.92])

popt, pcov = curve_fit(line, year, extent)
m = popt[0]         # gradient of best straight-line fit
b = popt[1]         # intercept

yearto2080 = np.arange(1979,2080)

print('extent(yr) = {:.3f}*year + {:.3f}'.format(m, b))
print('Estimate September sea-ice extent is 0 in year = {}'.format(int(-b/m)))
plt.plot(year, extent, 'o')
plt.plot(yearto2080, line(yearto2080, m, b), 'r')
plt.plot(-b/m,0,'gs')   # green square when ice extent is zero
plt.xlabel('Year')
plt.ylabel('September sea-ice extent (million sq km)')
plt.grid()
plt.show()