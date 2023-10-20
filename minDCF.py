import numpy as np
import matplotlib.pyplot as plt

def minDCF(Pmiss, Pfa, DET_limits, DCF_parameters):

    Cmiss = DCF_parameters[0]
    Cfa = DCF_parameters[1]
    Ptrue = DCF_parameters[2]
    Pfalse = DCF_parameters[3]
    npts = max(Pmiss.shape)
    if npts != max(Pfa.shape):
        raise Exception('vector size of Pmiss and Pfa not equal in call to Plot_DET')
    
    #-------------------------
    #Find DCF_best:
    
    DCF_vector = Cmiss * Pmiss * Ptrue  + Cfa * Pfa * Pfalse
    min_cost = np.amin(DCF_vector)
    min_ptr = (np.where(DCF_vector== np.amin(DCF_vector))[0])[0]
    Pmiss_opt = Pmiss[min_ptr]
    Pfa_opt = Pfa[min_ptr]
    
    return min_cost, Pmiss_opt, Pfa_opt

if __name__ == "__main__":   
    
    from set_DET_limits import set_DET_limits
    from compute_DET import compute_DET
    from setDCF import setDCF

    e6sIim = np.loadtxt(r'e9b/im_new.sc')
    e6sItr = np.loadtxt(r'e9b/tr_new.sc')
    
    [P_miss,P_fa] = compute_DET(e6sItr, e6sIim)
    Pmiss=P_miss
    Pfa = P_fa
    Pmiss_min = 0.01
    Pmiss_max = 0.45
    Pfa_min = 0.01
    Pfa_max = 0.45
    C_miss = 10
    C_fa = 1
    P_target = 0.01
    DET_limits = set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min, Pfa_max)
    DCF_parameters = setDCF (C_miss, C_fa, P_target)
