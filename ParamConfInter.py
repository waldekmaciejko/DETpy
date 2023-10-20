# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:54:20 2020

@author: Admin
"""
import numpy as np
########################################
import numpy as np
import time
import matplotlib.pyplot as plt

e6sIim = np.loadtxt(r'C:\badania\DETsrc\e9b\im_new.sc')
e6sItr = np.loadtxt(r'C:\badania\DETsrc\e9b\tr_new.sc')

clients=e6sItr;
imposteurs=e6sIim;
OPvalue = 0.5;
pas0=10000;

#################

m0 = max (clients)
num_clients = len(clients)
m1 = min (imposteurs)
num_imposteurs = len(imposteurs)
pas1 = (m0 - m1)/pas0
x=np.arange(m1,m0, pas1)
x=np.hstack((x, (x[-1]+pas1)))
num = len(x)

#a=time.time()
FRR = np.zeros([num])
FAR = np.zeros([num])
for i in range(0, num):
    fr=0
    fa=0
    for j in range(0, num_clients):
        if clients[j]<x[i]:
            fr=fr+1
    
    for k in range(0, num_imposteurs):
        if imposteurs[k]>=x[i]:
            fa=fa+1
    FRR[i] = 100*fr/num_clients    
    FAR[i] = 100*fa/num_imposteurs
    #print(i/num*100)
    
## calculation of EER value


tmp1 = np.where(FRR-FAR<=0)
tmps=len(tmp1);

if ((FAR[tmps]-FRR[tmps])<=(FRR[tmps+1]-FAR[tmps+1])):
    EER=(FAR[tmps]+FRR[tmps])/2
    tmpEER=tmps
else:
    EER=(FRR[tmps+1]+FAR[tmps+1])/2
    tmpEER=tmps+1

# calculation of the OP value

tmp2=np.where(OPvalue-FAR<=0)
tmpOP=len(tmp2)

OP=FRR[tmpOP]
########################################
#function [FARconfMIN  FRRconfMIN FARconfMAX FRRconfMAX]=ParamConfInter(FAR,FRR,num_imposteurs,num_clients)
#def = ParamConfInter(FAR,FRR,num_imposteurs,num_clients):

FAR=FAR
FRR=FRR
num_imposteurs = 25446
num_clients = 1754

# % function: ParamConfInter
# %
# % DESCRIPTION:
# % It calculates a 90% interval of confidence for each value of FAR and FRR
# % using a parametric method
# % 
# % INPUTS:
# % FAR: FAR vector
# % FAR: FRR vector
# % num_imposteurs: number of impostor tests
# % num_clients: number of client tests
# %
# % OUTPUTS:
# % FARconfMIN: vector of minimum values of FAR
# % FRRconfMIN: vector of minimum values of FRR
# % FARconfMAX: vector of maximum values of FAR
# % FRRconfMAX: vector of maximum values of FRR
# %
# %
# % CONTACT: aurelien.mayoue@int-edu.eu
# % 19/11/2007

# % size of error vectors
numErr = len(FAR)

# calculation of the confidence interval
FRRconfMIN = np.zeros([numErr])
FRRconfMAX = np.zeros([numErr])
FARconfMIN = np.zeros([numErr])
FARconfMAX = np.zeros([numErr])

for i in range(0,numErr):
    #varFRR=np.sqrt((FRR[i])*(1-FRR[i])/num_clients)
    print((FRR[i])*(1-FRR[i]))
    #FRRconfMIN[i]=FRR[i]-1.645*varFRR
    #FRRconfMAX[i]=FRR[i]+1.645*varFRR
    
    #varFAR=np.sqrt((FAR[i])*(1-FAR[i])/num_imposteurs)
    #FARconfMIN[i]=FAR[i]-1.645*varFAR    
    #FARconfMAX[i]=FAR[i]+1.645*varFAR
