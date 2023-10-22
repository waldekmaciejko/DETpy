import numpy as np

def set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min, Pfa_max):   
    
    """"
    helper function estimates baundaries values
    of DET curve
    """

    eps = np.finfo(float).eps # smallest float
    
    Pmiss_min = max(Pmiss_min,eps)
    Pmiss_max = min(Pmiss_max,1-eps)
    if Pmiss_max <= Pmiss_min:
        Pmiss_min = eps
        Pmiss_max = 1-eps

    Pfa_min = max(Pfa_min,eps)
    Pfa_max = min(Pfa_max,1-eps)
    if Pfa_max <= Pfa_min:
        Pfa_min = eps
        Pfa_max = 1-eps   
    
    DET_limits = [Pmiss_min, Pmiss_max, Pfa_min, Pfa_max];
    return DET_limits


if __name__ == '__main__':
    Pmiss_min = np.random.rand(1)
    Pmiss_max = np.random.rand(1)
    Pfa_min = np.random.rand(1)
    Pfa_max = np.random.rand(1)
    
    set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min, Pfa_max)
    