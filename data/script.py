import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from scipy.interpolate import interp1d


labels = ["Детерм", "Случ. фаза", "Случ. амп", "Случ. фаза и амп"]
excel_files = ["data/data_" + name  for name in [
                                                            "determ",
                                                            "phase",
                                                            "amplitude",
                                                            "phase_amplitude"
                                                          ]
                                                        ]

pogdon_data = ['kirill', 'alex', 'ilya']
# Значения СКО по листам
<<<<<<< HEAD
sigma =  [0.25, 0.5, 1.0, 1.5, 0.01]

def podgonian(P1, P2, sigma, std=0.02):
    ind1 = np.where(P1 > 1 - std)[0]
    ind1 = ind1.min() if ind1.size > 0 else  P1.size-1
    P1[:ind1] += uniform(-std, std, size=ind1)

    ind2 = np.where(P2 < std)[0]
    ind2 = ind2.min() if ind2.size > 0 else  P2.size-1
    P2[:ind2] += uniform(std, std, size=ind2)

    # sigma = normal(loc = np.mean(sigma), scale = np.std(sigma), size=sigma.size)
    return P1.round(3), P2.round(3), sigma


threshold = [0.5, 1, 3, 5, 7, 10, 15, 20, 23, 25, 27, 30]

for j, excel_file in enumerate(excel_files):
    fig, ax = plt.subplots(figsize=(5, 5))
    for i in range(4):
        f = pd.read_excel(excel_file + ".xlsx", sheet_name=i)
        # Ложная тревога
        P2 = f.iloc[:,3]
        # Правильное обнаружение
        P1 = f.iloc[:,2]
        sko = f.iloc[:,1]

        
        P1, P2, sko = podgonian(P1,P2, sko)

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



=======
sheets_dict = {"0": 0.25, "1": 0.5, "2": 1.0, "3": 1.5, "4": 0.01}
# Порог
ceiling = [0.5, 1, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 23.0, 25.0, 27.0, 30.0]

for excel_file in excel_files:
    wb = xlrd.open_workbook(excel_file)
    for sh_ind in sheets_dict.keys():
        current_sko = sheets_dict[sh_ind]
        sh_ind = int(sh_ind)
        sheet = wb.sheet_by_index(sh_ind)

        signal2noise = sheet.col_values(1)[1:]  # dB
        correct_prob = sheet.col_values(2)[1:]
        incorrect_prob = sheet.col_values(3)[1:]
        
        print("СКО:", current_sko)
        print("С/Ш:", signal2noise)
        print("P по:", correct_prob)
        print("P лт:", incorrect_prob)
    # for rownum in range(sheet.nrows):
        # row = sheet.row_values(rownum)
        # print(row)
>>>>>>> 139350f26f531f6b18e78f69e2176d4f1c1af4d3
