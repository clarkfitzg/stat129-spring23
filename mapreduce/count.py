import sys
import collections
import pickle

counts = collections.Counter(sys.stdin)

with open(sys.argv[1], 'wb') as f:
    pickle.dump(counts, f)
