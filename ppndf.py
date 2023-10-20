import numpy as np


def ppndf(cum_prob):
    
    SPLIT =  0.42
    
    A0 =   2.5066282388
    A1 = -18.6150006252
    A2 =  41.3911977353
    A3 = -25.4410604963
    B1 =  -8.4735109309
    B2 =  23.0833674374
    B3 = -21.0622410182
    B4 =   3.1308290983
    C0 =  -2.7871893113
    C1 =  -2.2979647913
    C2 =   4.8501412713
    C3 =   2.3212127685
    D1 =   3.5438892476
    D2 =   1.6370678189
    
    if np.size(cum_prob.shape) == 1:
        cum_prob = np.array([cum_prob])        
    
    [Nrows, Ncols] = cum_prob.shape
    
    norm_dev = np.zeros([Nrows, Ncols])
    eps_ = np.finfo(float).eps 
    
    cum_prob[np.where(cum_prob >= 1.0)[0]] = 1.0-eps_
    cum_prob[np.where(cum_prob <= 0.0)[0]] = eps_
    
    R = np.zeros([Nrows, Ncols])
    
    # adjusted prob matrix
    adj_prob=cum_prob-0.5
    
    centerindexes = np.where(abs(adj_prob) <= SPLIT)[0]
    tailindexes   = np.where(abs(adj_prob) > SPLIT)[0]
    
    R[centerindexes] = adj_prob[centerindexes] * adj_prob[centerindexes]
    
    norm_dev[centerindexes] = adj_prob[centerindexes] *(((A3 * \
                              R[centerindexes] + A2) * R[centerindexes] + \
                              A1) * R[centerindexes] + A0)
        
    norm_dev[centerindexes] = norm_dev[centerindexes] / ((((B4 * \
                              R[centerindexes] + B3) * R[centerindexes] + \
                              B2) * R[centerindexes] + B1) * \
                              R[centerindexes] + 1.0)
    
    right = np.where(cum_prob[tailindexes] > 0.5)[0]
    left  = np.where(cum_prob[tailindexes] < 0.5)[0]
    
    R[tailindexes] = cum_prob[tailindexes];
    R[tailindexes[right]] = 1 - cum_prob[tailindexes[right]]
    R[tailindexes] = np.sqrt((-1.0) * np.log(R[tailindexes]))
    
    norm_dev[tailindexes] = (((C3 * R[tailindexes] + C2) * \
                              R[tailindexes] + C1) * R[tailindexes] + C0)
    norm_dev[tailindexes] = norm_dev[tailindexes] / ((D2 * R[tailindexes] + \
                              D1) * R[tailindexes] + 1.0)
    
    norm_dev[tailindexes[left]] = norm_dev[tailindexes[left]] * -1.0;
    
    return norm_dev