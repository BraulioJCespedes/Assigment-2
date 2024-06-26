import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)

    #rmse
    return np.sqrt(np.mean((tar - pred) ** 2))