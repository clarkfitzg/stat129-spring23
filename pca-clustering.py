import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


good = "good happy joy fun sweet wonderful positive great".split()
bad = "bad terrible awful misery pain".split()

def gendoc(words, n=10):
    """
    Generate a string containing n elements from words,
    possibly repeated.
    """
    weights = np.linspace(1, 0.3, num=len(words))
    probs = weights / weights.sum()
    w = np.random.choice(words, n, p = probs)
    return " ".join(w)

ngood = 15
nbad = 10
good = [gendoc(good, 5) for x in range(ngood)]
bad = [gendoc(bad, 5) for x in range(nbad)]

corpus = good + bad

tf = TfidfVectorizer()

X = tf.fit_transform(corpus)
X.shape

# Experiment with this
ndim = 5
svd = TruncatedSVD(n_components=ndim, random_state=230)
svd.fit(X)

Xpc = svd.transform(X)

X.shape

Xpc.shape

svd.explained_variance_ratio_

plt.scatter(range(ndim), np.cumsum(svd.explained_variance_ratio_))
plt.xlabel('number of dimensions')
plt.ylabel('proportion of variance explained')


# Kmeans!

# Use ONLY the first npc components
npc = 2
Xsmall = Xpc[:, :npc]
Xsmall.shape

km = KMeans(n_clusters=2, random_state=2408)
predictions = km.fit_predict(Xsmall)

predictions

predictions[:ngood]

predictions[-nbad:]
