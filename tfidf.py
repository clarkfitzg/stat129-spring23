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
tfidfm = cv.fit_transform(corpus)

# Last row:
last = dtm[-1, :]

terms = cv.get_feature_names()

_, col = last.nonzero()

for i in col:
    print(terms[i])


mostfreq = counts.argsort()
mostfreq = np.squeeze(np.array(mostfreq))

for i in mostfreq[::-1]:
    #print(i)
    print(terms[i])


