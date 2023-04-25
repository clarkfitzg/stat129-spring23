
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Run in ipython:
#%matplotlib inline

# Random normal points
Z = np.random.standard_normal(size = (10, 2))

plt.plot(Z[:, 0], Z[:, 1])

# Move the center of the last 5 to (5, 3)
Z[-5:, 0] += 5
Z[-5:, 1] += 3

plt.plot(Z[:, 0], Z[:, 1])

km = KMeans(2)
clusters = km.fit_predict(Z)


