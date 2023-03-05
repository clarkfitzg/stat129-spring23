# Replaces shell pipeline 

# sort | uniq -c 

# with a more efficient algorithm

import csv
import sys
from collections import Counter

counts = Counter(sys.stdin)

writer = csv.writer(sys.stdout)
for val, count in counts.items():
    value = val.strip()
    writer.writerow((value, count))
