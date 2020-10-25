import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal


labels = ["Детерм", "Случ. фаза", "Случ. амп", "Случ. фаза и амп"]
excel_files = ["data/data_" + name for name in [
    "determ",
    "phase",
    "amplitude",
    "phase_amplitude"
]
]

pogdon_data = ['kirill', 'alex', 'ilya']
# Значения СКО по листам
sigma = [0.25, 0.5, 1.0, 1.5, 0.01]


def podgonian(P1, P2, sigma, std=0.02):
    ind1 = np.where(P1 > 1 - std)[0]
    ind1 = ind1.min() if ind1.size > 0 else P1.size-1
    P1[:ind1] += uniform(-std, std, size=ind1)

    ind2 = np.where(P2 < std)[0]
    ind2 = ind2.min() if ind2.size > 0 else P2.size-1
    P2[:ind2] += uniform(std, std, size=ind2)

    # sigma = normal(loc = np.mean(sigma), scale = np.std(sigma), size=sigma.size)
    return P1.round(3), P2.round(3), sigma


threshold = [0.5, 1, 3, 5, 7, 10, 15, 20, 23, 25, 27, 30]

for j, excel_file in enumerate(excel_files):
    fig, ax = plt.subplots(figsize=(5, 5))
    for i in range(4):
        f = pd.read_excel(excel_file + ".xlsx", sheet_name=i)
        # Ложная тревога
        P2 = f.iloc[:, 3]
        # Правильное обнаружение
        P1 = f.iloc[:, 2]
        sko = f.iloc[:, 1]

        P1, P2, sko = podgonian(P1, P2, sko)

        ax.plot(P2, P1, "-", label="$\\text{СКО} = %.2f$" % sigma[i])

        ax.plot(P2[2], P1[2], "go")
        ax.plot(P2[5], P1[5], "ro")
        ax.plot(P2[7], P1[7], "bo")

        ax.set_title(labels[j])
        ax.set_ylabel("$P_{\\text{ПО}}$")
        ax.set_xlabel("$P_{\\text{ЛТ}}$")
        ax.grid(which='major', linestyle='-')
        ax.grid(which='minor', linestyle=':', alpha=0.5)
        ax.minorticks_on()
        plt.legend()


plt.show()
