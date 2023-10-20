import numpy as np

def DETsort(scores):
    
    """
    sort values of scores
    """
    
    s=scores[np.lexsort(np.fliplr(scores).T)]
    
    return s

