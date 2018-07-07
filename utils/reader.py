import numpy as np
from scipy.sparse import csr_matrix

def read_graph(path):
    X = np.loadtxt(path, dtype=int, comments='%')
    m, n = X.shape

    if n == 2:
        # the graph is unweighted
        X = np.c_[ X, np.ones(m) ]
    elif n <= 1 or n >= 4:
        # undefined type, invoerror
        _

    base = np.amin(X[:, 0:2])
    X[:, 0:2] = X[:, 0:2] - base

    row  = X[:, 0]
    col  = X[:, 1]
    data = X[:, 2]

    n = int(np.amax(X[:, 0:2]) + 1) # assume id starts from 0

    A = csr_matrix((data, (row, col)), shape=(n, n))

    return A

if __name__ == "__main__":
    path = './data/sample.tsv'
    read_graph(path)

