import re
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["hello world", "hello beautiful", "hello world traveler hello"]

cv = CountVectorizer()

# document term matrix 
dtm = cv.fit_transform(corpus)

# Sum along the columns to find the most frequent words
counts = dtm.sum(axis=0)

tf = TfidfVectorizer()

# document term matrix 
dtm = cv.fit_transform(corpus)

# Apply a regular expression to find a special row.
# If you don't find anything, then make your regular expression less specific
for i, doc in enumerate(corpus):
    if re.search("world traveler", doc):
        break

row = dtm[i, :]

terms = cv.get_feature_names()

_, col = row.nonzero()

# These terms should match up
print("Original document: ", doc)
print("""

Words in matrix:
----------------""")
for i in col:
    print(terms[i])


# Find the most frequent wording s
mostfreq = counts.argsort()
mostfreq = np.squeeze(np.array(mostfreq))
for i in mostfreq[::-1]:
    print(terms[i])
