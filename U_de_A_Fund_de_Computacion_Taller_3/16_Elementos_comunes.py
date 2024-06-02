import numpy as np

def valores_unicos(a, b):
    return np.in1d(a, np.intersect1d(a,b))

a = np.array([0,  10,  20,  40,  60])
b = np.array([0, 40])

print(valores_unicos(a,b))