from set_DET_limits import set_DET_limits
import numpy as np
import matplotlib.pyplot as plt
from ppndf import ppndf
import matplotlib
from minDCF import minDCF
from setDCF import setDCF


def make_DET(Pmiss, Pfa, EER):
    """
    plot DET characteristic
    """

    pticks = [0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005,
              0.001, 0.002, 0.005, 0.01, 0.02, 0.05,
              0.1, 0.2, 0.4, 0.6, 0.8, 0.9,
              0.95, 0.98, 0.99, 0.995, 0.998, 0.999,
              0.9995, 0.9998, 0.9999, 0.99995, 0.99998, 0.99999]

    # xlabels = [ [' 0.001',  ' 0.002',  ' 0.005',  ' 0.01 ',  ' 0.02 ',  ' 0.05 '],
    #             [ '  0.1 ',  '  0.2 ',  ' 0.5  ',  '  1   ',  '  2   ',  '  5   '],
    #             ['  10  ',  '  20  ',  '  40  ',  '  60  ',  '  80  ',  '  90  '],
    #             ['  95  ',  '  98  ',  '  99  ',  ' 99.5 ',  ' 99.8 ',  ' 99.9 '],
    #             [' 99.95',  ' 99.98',  ' 99.99',  '99.995',  '99.998',  '99.999']]

    labels = [' 0.001', ' 0.002', ' 0.005', ' 0.01 ', ' 0.02 ', ' 0.05 ',
              '  0.1 ', '  0.2 ', ' 0.5  ', '  1   ', '  2   ', '  5   ',
              '  10  ', '  20  ', '  40  ', '  60  ', '  80  ', '  90  ',
              '  95  ', '  98  ', '  99  ', ' 99.5 ', ' 99.8 ', ' 99.9 ',
              ' 99.95', ' 99.98', ' 99.99', '99.995', '99.998', '99.999']

    Pmiss_min = 0.01
    Pmiss_max = 0.45
    Pfa_min = 0.01
    Pfa_max = 0.45

    DET_limits = set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min, Pfa_max)

    Pmiss_min = DET_limits[0]
    Pmiss_max = DET_limits[1]
    Pfa_min = DET_limits[2]
    Pfa_max = DET_limits[3]

    ntick = len(pticks)
    for n in range(ntick - 1, -1, -1):
        if (Pmiss_min <= pticks[n]):
            tmin_miss = n
        if (Pfa_min <= pticks[n]):
            tmin_fa = n

    for n in range(0, ntick, 1):
        if (pticks[n] <= Pmiss_max):
            tmax_miss = n
        if (pticks[n] <= Pfa_max):
            tmax_fa = n

    ylabels = labels
    xlabels = labels

    # estimate minimal Cost Function - minDCF
    C_miss = 10
    C_fa = 1
    P_target = 0.01
    DCF_parameters = setDCF(C_miss, C_fa, P_target)
    DET_limits = set_DET_limits(Pmiss_min, Pmiss_max, Pfa_min, Pfa_max)
    min_cost, Pmiss_opt, Pfa_opt = minDCF(Pmiss, Pfa, DET_limits, DCF_parameters)

    # plot
    matplotlib.rcParams.update({'font.size': 26})
    ax = plt.subplot()
    ax.plot(ppndf(Pmiss), ppndf(Pfa), linestyle='--', c='g', linewidth=3, markersize=3, label='DET')
    ax.plot(ppndf(Pmiss_opt), ppndf(Pfa_opt), marker='o', c='r', linewidth=20, markersize=15, label='minDCF')
    ax.plot(ppndf(EER), ppndf(EER), marker='o', c='g', linewidth=20, markersize=15, label='EER')

    ax.set_xlim(ppndf(np.array([[Pfa_min], [Pfa_max]])))
    ax.set_xticks(ppndf(np.array([pticks[tmin_fa:tmax_fa]]).T).reshape(-1), xlabels[tmin_fa:tmax_fa])
    ax.set_xlabel('False Alarm probability (%)')
    ax.set_ylim(ppndf(np.array([[Pmiss_min], [Pmiss_max]])))
    ax.set_yticks(ppndf(np.array([pticks[tmin_miss:tmax_miss]]).T).reshape(-1), ylabels[tmin_miss:tmax_miss])
    ax.set_ylabel ('Miss probability (%)')
    ax.legend()
    ax.grid(visible=True, which='major', axis='both', linestyle='-')
    ax.grid(visible=True, which='minor', axis='both', linestyle='--')

    plt.show()

    return  Pmiss_opt, Pfa_opt


if __name__ == "__main__":
    from compute_DET import compute_DET
    from EER_DET import EER_DET_conf

    e6sIim = np.loadtxt(r"e9b/im_new.sc")
    e6sItr = np.loadtxt(r"e9b/tr_new.sc")

    [EERplot, x, FRR, FAR] = EER_DET_conf(e6sItr, e6sIim, 0.5, 10000)

    Pmiss_min = 0.01
    Pmiss_max = 0.45
    Pfa_min = 0.01
    Pfa_max = 0.45

    [P_miss, P_fa] = compute_DET(e6sItr, e6sIim)

    # plot Detection Error Tradeoff plot - DET
    linestyle = 'g--'
    lw = 3
    fon_siz = 26
    m = 3
    make_DET(P_miss, P_fa, EERplot)

