"""
Which stations have complete observations in both the first and the last years?
"""

import collections
import csv
import gzip

# TODO: look up the last few columns
FIELDNAMES = "station date element value 4 5 6 7".split()

def stations(datafile='/stat129/1900.csv.gz', element="TMAX"):
    with gzip.open(datafile, mode='rt') as f:
        stream = csv.DictReader(f, fieldnames=FIELDNAMES)
        for x in stream:
            if x['element'] == element:
                yield x['station']


def fullyear(**kwargs):
    stn = collections.Counter(stations(**kwargs))
    full = {x for x, count in stn.items() if count == 365}
    return full


s1900 = fullyear(datafile='/stat129/1900.csv.gz')
s2020 = fullyear(datafile='/stat129/2020.csv.gz')

# Only 23!!!
both = s1900.intersection(s2020)

with open("TMAXstn", "w") as f:
    for stn in both:
        print(stn, file=f)
