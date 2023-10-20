import numpy as np
import matplotlib.pyplot as plt

from set_DET_limits import set_DET_limits
from compute_DET import compute_DET
#from ppndf import ppndf
from make_DET import make_DET
from setDCF import setDCF
from minDCF import minDCF
from EER_DET import EER_DET_conf

e6sIim = np.loadtxt(r"e9b/im_new.sc")
e6sItr = np.loadtxt(r"e9b/tr_new.sc")

thickness = 2.5

Pmiss_min = 0.01;
Pmiss_max = 0.45;
Pfa_min = 0.01;
Pfa_max = 0.45;

[P_miss, P_fa] = compute_DET(e6sItr, e6sIim)

# plot Detection Error Tradeoff plot - DET
linestyle = 'g--'
lw=3
fon_siz=26
m=3
make_DET(P_miss, P_fa, linestyle, lw, fon_siz, m)
print("30")

# estimate minimal Cost Function - minDCF
C_miss = 10
C_fa = 1
P_target = 0.01
DCF_parameters = setDCF(C_miss, C_fa, P_target)
DET_limits = set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min,Pfa_max)
[min_cost, Pmiss_opt, Pfa_opt] = minDCF(P_miss, P_fa, DET_limits, DCF_parameters)

print("40")

linestyle = 'ro'
lw=20
fon_siz=26
m=15
make_DET(Pmiss_opt, Pfa_opt, linestyle, lw, fon_siz, m)
print(f'Pmiss_opt: {Pmiss_opt[0]*100}')
print(f'Pfa_opt: {Pfa_opt[0]*100}')

print("50")

# estimate Equal Error Rate
linestyle = 'go'
lw=20
fon_siz=26
m=15
[EERplot, x, FRR, FAR] = EER_DET_conf(e6sItr,e6sIim, 0.5,10000)
make_DET(EERplot, EERplot, linestyle, lw, fon_siz, m)
print('EER:', EERplot[0]*100)

# plot False Acceptance Rate agains False Rejection Rate - FAR vs FRR
plt.figure(2)
plt.plot (x,FRR,'r')
plt.plot (x,FAR,'b')
plt.xlabel ('Threshold')
plt.ylabel ('Error');
plt.title ('FAR vs FRR graph')
plt.grid(axis='both')

# plot ROC curve
plt.figure(3)
plt.plot (FAR,100-FRR,'r');
plt.xlabel ('Impostor Attempts Accepted = FAR (%)');
plt.ylabel ('Genuine Attempts Accepted = 1-FRR (%)');
plt.title ('ROC curve');
plt.grid(axis='both')

################################### EER point
#plt.scatter(EERplot[0],100-EERplot[0],'ok');







