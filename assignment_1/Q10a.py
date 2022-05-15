import numpy as np
import pandas as pd

mydata = pd.read_csv("latlong.csv")

code = mydata['code'].values
country = mydata['country'].values
latdeg = mydata['latdeg'].values
latmin = mydata['latmin'].values
longdeg = mydata['longdeg'].values
longmin = mydata['longmin'].values


def sphericaldistance(phi1, lambda1, phi2, lambda2):
    """Given two points on the Earth's surface defined by
    (latitude,longitude) coordinates (phi1,lambda1) and (phi2,lambda2),
    this function returns the spherical distance (km) between those
    points. Latitude and longitude are specified in degrees north
    of the equator and east of Greenwich meridian, respectively.
    Negative values for latitude/longitude correspond to degrees
    south of the equator and west of Greenwich meridian, respectively.
    The spherical distance is computed using formula (15) in the
    assignment sheet.

    Ref: https://en.wikipedia.org/wiki/Great-circle_distance#Computational_formulas

    Example: sphericaldistance(38.833333333333336, -77.0,
                                45.333333333333336 -75.66666666666667)
            returns 731.064055709268
    """

    r = 6371  # Earth radius (km)
    dlambda = np.abs(lambda1 - lambda2)  # equation (14)

    # cos/sin terms to simplify equation (15)
    cos1 = np.cos(np.pi * phi1 / 180)
    sin1 = np.sin(np.pi * phi1 / 180)
    cos2 = np.cos(np.pi * phi2 / 180)
    sin2 = np.sin(np.pi * phi2 / 180)

    # equation (15)
    num = np.sqrt(
        (cos2 * np.sin(np.pi * dlambda / 180)) ** 2 + (cos1 * sin2 - sin1 * cos2 * np.cos(np.pi * dlambda / 180)) ** 2)
    den = sin1 * sin2 + cos1 * cos2 * np.cos(np.pi * dlambda / 180)

    return r * np.arctan2(num, den)


def idx2latlong(i):
    """Given a row index into the latlong.csv spreadsheet (first data
    row after header is index 0), this function returns the associated
    capital city latitude and longitude (both in degrees), and the
    length-3 country string.

    Example: idx2latlong(193) returns -35.03333333333333, 149.16666666666666, 'AUL'
    """

    if latdeg[i] >= 0:      # degrees north of the equator
        lat = latdeg[i] + latmin[i] / 60.
    else:                   # degrees south
        lat = latdeg[i] - latmin[i] / 60.
    if longdeg[i] >= 0:     # degrees east of Greenwich meridian
        long = longdeg[i] + longmin[i] / 60.
    else:                   # degrees west
        long = longdeg[i] - longmin[i] / 60.
    return lat, long, country[i]


# -------------------------------------------------------------------
#   MAIN
# -------------------------------------------------------------------
# Calculate distance between two pairs of capital cities, for which
# data is presented in the question sheet:
#
# Distance between capitals of USA and CAN: 731.06 km
# Distance between capitals of USA and AUL: 15933.50 km

lat0, long0, country0 = idx2latlong(0)              # 0 == index for USA
lat1, long1, country1 = idx2latlong(1)              # 1 == index for CAN
lat193, long193, country193 = idx2latlong(193)      # 193 == index for AUL

# first pair of capitals: USA & CAN
d = sphericaldistance(lat0, long0, lat1, long1)
print("Distance between capitals of {} and {}: {:.2f} km".format(country0, country1, d))

# second pair of capitals: USA & AUL
d = sphericaldistance(lat0, long0, lat193, long193)
print("Distance between capitals of {} and {}: {:.2f} km".format(country0, country193, d))
