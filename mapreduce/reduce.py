import os
import sys
import collections
import pickle

# temporary results for each file are stored
files = ['counts/' + f for f in os.listdir('counts')]

# store final result here
result = collections.Counter()

# Update by including the counts for all
for fname in files:
    with open(fname, 'rb') as f:
        result = result + pickle.load(f)

# Write final counts to stdout
for count, value in result.items():
    print(count.strip() + "  " + value)
