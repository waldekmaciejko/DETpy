import numpy as np
import matplotlib.pyplot as plt

#from set_DET_limits import set_DET_limits
from compute_DET import compute_DET
#from ppndf import ppndf
from make_DET import make_DET
#from setDCF import setDCF
#from minDCF import minDCF
from EER_DET import EER_DET_conf

e6sIim = np.loadtxt(r"e9b/im_new.sc")
e6sItr = np.loadtxt(r"e9b/tr_new.sc")

thickness = 2.5

Pmiss_min = 0.01;
Pmiss_max = 0.45;
Pfa_min = 0.01;
Pfa_max = 0.45;

Pmiss, Pfa = compute_DET(e6sItr, e6sIim)
[EERplot, x, FRR, FAR] = EER_DET_conf(e6sItr, e6sIim, 0.5,10000)
Pmiss_opt, Pfa_opt = make_DET(Pmiss, Pfa, EERplot)

print(f'Pmiss_opt: {Pmiss_opt[0]*100}')
print(f'Pfa_opt: {Pfa_opt[0]*100}')
print('EER:', EERplot[0]*100)

#-----------------
# plot False Acceptance Rate agains False Rejection Rate - FAR vs FRR
plt.figure(2)
plt.plot (x,FRR,'r')
plt.plot (x,FAR,'b')
plt.xlabel ('Threshold')
plt.ylabel ('Error');
plt.title ('FAR vs FRR graph')
plt.grid(axis='both')
plt.show()

# plot ROC curve
plt.figure(3)
plt.plot (FAR,100-FRR,'r');
plt.xlabel ('Impostor Attempts Accepted = FAR (%)');
plt.ylabel ('Genuine Attempts \nAccepted = 1-FRR (%)');
plt.title ('ROC curve');
plt.grid(axis='both')
plt.show()









