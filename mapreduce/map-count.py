import collections
import os
import pickle
import sys

counts = collections.Counter(sys.stdin)

# file to store temporary results.
tempfile = 'counts/' + os.path.basename(sys.argv[1]) + '.pickle'

with open(tempfile, 'wb') as f:
    pickle.dump(counts, f)
