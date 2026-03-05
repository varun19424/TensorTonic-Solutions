import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # y_pred = np.array(y_pred)
    # y_true = np.array(y_true)
    # # Write code here
    # if len(y_pred) == len(y_true):
    #     return (np.sum((y_pred-y_true)**2))/len(y_pred)
    p = len(y_pred)
    if len(y_pred) == len(y_true):
        return sum([(n - m)*(n - m) for n , m in zip(y_pred ,y_true)])/p

    return None
