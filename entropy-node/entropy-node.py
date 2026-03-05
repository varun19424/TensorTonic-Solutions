import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    count = np.bincount(y)
    prob = count / len(y)
    prob = prob[prob > 0]
    h = -np.sum(prob * np.log2(prob))
    return h