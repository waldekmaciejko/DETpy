import numpy as np
from DETsort import DETsort

def compute_DET(true_scores, false_scores):
 
    SMAX = 9E99
    num_true = len(true_scores)
    num_false = len(false_scores)
    
    total=num_true+num_false;
    
    Pmiss = np.zeros([num_true+num_false+1, 1]); #preallocate for speed
    Pfa   = np.zeros([num_true+num_false+1, 1]); #preallocate for speed
    
    P=Pmiss
    scores = np.zeros([total, 2])
    scores[0:num_false,0] = false_scores
    scores[0:num_false,1] = 0
    scores[num_false:total,0] = true_scores
    scores[num_false:total,1] = 1
    
    scores=DETsort(scores);
    sumtrue=np.cumsum(scores[:,1])
    sumfalse=num_false - (np.arange(1, total+1, 1) - sumtrue)
    Pmiss[0] = 0
    Pfa[0] = 1.0
    
    Pmiss[1:total+1,0] =sumtrue/num_true
    Pfa[1:total+1,0] = sumfalse/num_false;
    
    return Pmiss, Pfa

if __name__ == "__main__":

    false_scores = np.loadtxt(r'e9b/im_new.sc')
    true_scores = np.loadtxt(r'e9b/tr_new.sc')
    
    compute_DET(true_scores, false_scores)

