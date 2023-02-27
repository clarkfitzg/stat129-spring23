import csv
import glob
import gzip
import itertools


def weather(datafile='/stat129/1900.csv.gz'):
    """
    Generator for every observation in the datafile
    """
    # TODO: look up the last few columns
    FIELDNAMES = "station date element value 4 5 6 7".split()
    with gzip.open(datafile, mode='rt') as f:
        stream = csv.DictReader(f, fieldnames=FIELDNAMES)
        yield from stream


def allweather(datafiles='/stat129/*.csv.gz'):
    """
    Generator for ALL the weather observations
    """
    full_file_paths = glob.glob(datafiles)
    allstreams = map(weather, full_file_paths)
    combined = itertools.chain(*allstreams)
    yield from combined


# Mon Feb 27 06:50:47 UTC 2023
# Select TMAX observations from Oxford, which seem to be complete
STN_ID="UK000056225"

with open("oxford_tmax.csv", "w") as f:
    fieldnames = ['year', 'date', 'tmax']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for obs in allweather():
        #for obs in weather():
        if obs["station"] == STN_ID and obs["element"] == "TMAX":
            row = {"year": obs["date"][:4],
                    "date": obs["date"][4:],
                    "tmax": obs["value"],
                    }
            writer.writerow(row)

