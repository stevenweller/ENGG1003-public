import numpy as np
import pandas as pd

# -------------------------------------------------------------------
#   READ DATA FROM TWO SPREADSHEETS PROVIDED
# -------------------------------------------------------------------
# latlong.csv
# latitude, longitude, numerical code and length-3 country string
# for 203 capital cities

mydata = pd.read_csv("latlong.csv")

latdeg = mydata['latdeg'].values
latmin = mydata['latmin'].values
longdeg = mydata['longdeg'].values
longmin = mydata['longmin'].values
code = mydata['code'].values
country = mydata['country'].values

# capdist.csv
# distances between 202 x 203 = 41006 distinct pairs of capital cities,
# each pair of cities being identified by the pair of numerical codes
# defined in latlong.csv

mydata = pd.read_csv("capdist.csv")

codea = mydata['numa'].values
codeb = mydata['numb'].values
kmdist = mydata['kmdist'].values


# -------------------------------------------------------------------
#   SPHERICALDISTANCE()
# -------------------------------------------------------------------
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

    r = 6371                                # Earth radius (km)
    dlambda = np.abs(lambda1 - lambda2)     # equation (14)

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


# -------------------------------------------------------------------
#   IDX2LATLONG()
# -------------------------------------------------------------------
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
#   CODE2IDX()
# -------------------------------------------------------------------
def code2idx(targetcode):
    """Given a numerical country code as defined in latlong.csv,
    this function returns the corresponding row index in latlong.csv

    Examples:   code2idx(2) returns 0 (USA)
                code2idx(20) returns 1 (CAN)
                code2idx(900) returns 193 (AUL)
    """

    found = False
    i = 0
    while not found:
        if code[i] == targetcode:
            found = True
            idx = i
        else:
            i += 1
    return idx


# -------------------------------------------------------------------
#   MAIN
# -------------------------------------------------------------------
# Calculate distance between all 203 x 202 = 41006 city-pairs in
# capdist.csv spreadsheet. Determine and display largest discrepancy
# between any city-pair distance calculated using spherical distance
# formula (15) in assignment sheet, and the corresponding distance
# reported in capdist.csv

maxdiscrep = 0
for i in range(0, len(kmdist)):
    lata, longa, countrya = idx2latlong(code2idx(codea[i]))
    latb, longb, countryb = idx2latlong(code2idx(codeb[i]))

    dist_a_b = sphericaldistance(lata, longa, latb, longb)

    discrepancy = np.abs(kmdist[i] - dist_a_b)
    if discrepancy > maxdiscrep:
        maxdiscrep = discrepancy
        idx = i

# display largest discrepancy
lata, longa, countrya = idx2latlong(code2idx(codea[idx]))
latb, longb, countryb = idx2latlong(code2idx(codeb[idx]))
print("Maximum discrepancy = {:.4f} km".format(maxdiscrep))
print("City pair: {}, {}".format(countrya, countryb))
