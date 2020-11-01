import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from scipy.special import erf


labels = ["Детерминированный", "Случайная фаза",
          "Случайная амплитуда", "Случайная фаза и амплитуда"]
excel_files = ["data/data_" + name for name in [
    "determ",
    # "phase",
    # "amplitude",
    "phase_amplitude"
]
]

pogdon_data = ['kirill', 'alex', 'ilya']
# Значения СКО по листам
sigma = [0.25, 0.5, 1.0, 1.5, 0.01]
signal_length = 64
signal_amp = 2


Laplace = lambda y: 1/2*(erf(y/np.sqrt(2)) + 1)

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
thr = np.logspace(np.log10(1e-9), np.log10(1000), 300)

for j, excel_file in enumerate(excel_files):
    fig, ax = plt.subplots(figsize=(5, 5))
    for i in range(4):
        f = pd.read_excel(excel_file + ".xlsx", sheet_name=i)
        # Ложная тревога
        P2 = f.iloc[:, 3]
        # Правильное обнаружение
        P1 = f.iloc[:, 2]
        snr = f.iloc[:, 1]
        snr_mean = np.mean(snr)
        snr_nat = 10**(snr_mean/10)
        print("Средний С/Ш:", snr_mean, 'дБ')
        print("Средний С/Ш:", snr_nat)

        # P1, P2, snr = podgonian(P1, P2, snr)

        # Теория
        N_0 = sigma[i]**2                             # СПМ шума
        E_s = 0.5 * signal_amp**2 * signal_length     # Энергия сигнала
        # d = np.sqrt(2 * E_s/N_0)
        d = np.sqrt(4 * snr_nat)
        P2_t = 1 - Laplace(np.log(thr)/d + d/2)       # Теория ЛТ
        P1_t = 1 - Laplace(np.log(thr)/d - d/2)       # Теория ПО
        
        print(P2_t, P1_t, d)
        ax.plot(P2_t, P1_t, "--", label="СКО = %.2f. Теория" % sigma[i])
        ax.plot(P2, P1, ".-", label="СКО = %.2f" % sigma[i])
        # ax.plot(P2_t, P1_t, label="$\\text{СКО} = %.2f$. Теория" % sigma[i])
        # ax.plot(P2, P1, ".-", label="$\\text{СКО} = %.2f$" % sigma[i])


        # ax.plot(P2[2], P1[2], "o", color="darkblue", zorder=3)
        # ax.plot(P2[5], P1[5], "s", color="darkblue", zorder=3)
        # ax.plot(P2[7], P1[7], "^", color="darkblue", zorder=3)

        ax.set_title(labels[j])
        # ax.set_ylabel("$P_{\\text{ПО}}$")
        # ax.set_xlabel("$P_{\\text{ЛТ}}$")
        ax.grid(which='major', linestyle='-')
        ax.grid(which='minor', linestyle=':', alpha=0.5)
        ax.minorticks_on()
        plt.legend()

    plt.savefig('%s.pdf' % excel_file)

plt.show()



