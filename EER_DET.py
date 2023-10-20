import numpy as np

def EER_DET_conf(clients, impostors, OPvalue, pas0):
    
    m0 = max (clients)
    num_clients = len(clients)
    m1 = min (impostors)
    num_imposteurs = len(impostors)
    pas1 = (m0 - m1)/pas0
    x=np.arange(m1, m0, pas1)
    x=np.hstack((x, (x[-1] + pas1)))
    num = len(x)
    
    #a=time.time()
    FRR = np.zeros([num])
    FAR = np.zeros([num])
    for i in range(0, num):
        fr=0
        fa=0
        for j in range(0, num_clients):
            if clients[j] < x[i]:
                fr = fr + 1
        
        for k in range(0, num_imposteurs):
            if impostors[k]>=x[i]:
                fa=fa + 1
        FRR[i] = 100*fr/num_clients    
        FAR[i] = 100*fa/num_imposteurs
        
    ## calculation of EER value
    
    
    tmp1 = np.where(FRR-FAR<=0)[0]
    tmps=len(tmp1)
    
    if ((FAR[tmps] - FRR[tmps]) <= (FRR[tmps+1] - FAR[tmps+1])):
        EER=(FAR[tmps] + FRR[tmps])/2
        tmpEER = tmps
    else:
        EER = (FRR[tmps+1]+FAR[tmps+1])/2
        tmpEER = tmps+1
    
    # calculation of the OP value
    
    tmp2 = np.where(OPvalue-FAR<=0)[0]
    tmpOP = len(tmp2)
    
    #OP = FRR[tmpOP]
    
    equaX = x[tmps]*(FRR[tmps+1] - FAR[tmps+1]) + x[tmps+1] * (FAR[tmps] - FRR[tmps])
    equaY = FRR[tmps+1] - FAR[tmps+1] + FAR[tmps] - FRR[tmps]
    threshold = equaX/equaY
    EERplot = threshold * (FAR[tmps] - FAR[tmps+1])/(x[tmps] - x[tmps+1]) + \
        (x[tmps] * FAR[tmps+1] - x[tmps+1] * FAR[tmps]) / (x[tmps] - x[tmps+1])
    EERplot = np.array([EERplot/100])
    
    return EERplot, x, FRR, FAR

if __name__ == "__main__":
    
    impostor = np.loadtxt(r'C:\badania\DETsrc\e9b\im_new.sc')
    clients = np.loadtxt(r'C:\badania\DETsrc\e9b\tr_new.sc')

    OPvalue = 0.5
    pas0=10000
    
    EER_DET_conf(clients, impostor, OPvalue, pas0)


            