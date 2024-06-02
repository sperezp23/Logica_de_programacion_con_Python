import numpy as np

def sumar_pares(arreglo_enteros):
    return arreglo_enteros[arreglo_enteros % 2 == 0].sum()

print(sumar_pares(np.arange(0, 100, dtype = int)))
