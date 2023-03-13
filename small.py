import csv # pandas is fine too
import sys
import gzip
import statistics


# Create a dictionary with a list of numbers corresponding to each station
stations = {"AGE00135039": [], "AGE00147705": []}

with gzip.open("small.csv.gz", mode="rt") as f:
    stream = csv.reader(f)
    for row in stream:
        stn = row[0]
        element = row[2]
        if stn in stations and element == "TMAX":
            tmax_obs = int(row[3])
            # Add the relevant TMAX observation
            stations[stn].append(tmax_obs)

# Results
for stn, tmax_obs in stations.items():
    print(stn, statistics.median(tmax_obs))
