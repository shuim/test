import numpy as np
from sklearn.decomposition import NMF

X = [
        [1, 1, 2, 3, 1],
        [0, 1, 0, 1, 1],
        [2, 0, 4, 4, 0],
        [3, 0, 6, 6, 0],
    ]

nmf = NMF(n_components=2)
nmf.fit(X)

print(np.round(nmf.components_, 1))
print(np.round(nmf.transform(X), 1))
print(np.round(np.dot(nmf.transform(X), nmf.components_), 1))