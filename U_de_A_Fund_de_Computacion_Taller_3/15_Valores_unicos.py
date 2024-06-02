import numpy as np

def valores_unicos(a, b):
    return a[~np.in1d(a, np.intersect1d(a,b))]

a = np.array([0,  10,  20,  40,  60,  80])
b = np.array([10,  30,  40,  50,  70])

print(valores_unicos(a,b))