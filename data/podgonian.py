
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform
from scipy.interpolate import interp1d

def podgonian(P1, P2, std=0.02):
    ind1 = np.where(P1 > 1 - std)[0]
    ind1 = ind1.min() if ind1.size > 0 else  P1.size-1
    P1[:ind1] += uniform(0, 0.02, size=ind1)

    ind2 = np.where(P2 < std)[0]
    ind2 = ind2.min() if ind2.size > 0 else  P2.size-1
    P2[:ind2] += uniform(0, 0.02, size=ind2)
    return P1, P2