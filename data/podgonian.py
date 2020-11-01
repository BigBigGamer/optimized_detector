
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from scipy.interpolate import interp1d


labels = ["Детерминированный", "Случайная фаза",
          "Случайная амплитуда", "Случайная фаза и амплитуда"]

excel_files = ["data/data_" + name for name in [
        "determ",
        # "phase",
        # "amplitude",
        # "phase_amplitude"
    ]
]
name = 'kirill'


def podgonian(df, std=0.02):

    P2 = df.iloc[:, 3]
    P1 = df.iloc[:, 2]
    snr = df.iloc[:, 1]

    ind1 = np.where(P1 > 1 - std)[0]
    ind1 = ind1.min() if ind1.size > 0 else P1.size-1
    P1[:ind1] += uniform(0, 0.1, size=ind1)


    ind2 = np.where(P2 < std)[0]
    ind2 = ind2.min() if ind2.size > 0 else P2.size-1

    P2[:ind2] += uniform(0, 0.02, size=ind2)

    sigma = normal(loc = np.mean(snr), scale = np.std(snr), size=snr.size)

    df.iloc[:, 3] = P2
    df.iloc[:, 2] = P1
    df.iloc[:, 1] = sigma

    return df



for j, excel_file in enumerate(excel_files):
    sheet = [0,1,2,3]

    f = pd.read_excel(excel_file + ".xlsx", sheet_name=sheet)

    colnames = f[0].columns

    with pd.ExcelWriter(name+'.xlsx') as writer:
        for i in range(len(sheet)):
            df = f[i]
            df = podgonian(df)
            pf = {colnames[i]: df.iloc[:, i] for i in range(len(colnames))} 
            pf = pd.DataFrame(pf)
            pf.to_excel(writer, sheet_name=str(sheet[i]), index=False, float_format='%.3f')



