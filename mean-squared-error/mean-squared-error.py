import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred_arr = np.array(y_pred)
    y_true_arr = np.array(y_true)
    if len(y_pred_arr) == len(y_true_arr):
        return np.sum((y_pred_arr-y_true_arr)**2)/len(y_true_arr)
    return None
