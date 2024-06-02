import numpy as np

def unos_borde_ceros_centro(n: int):
    '''
    Toma como parámetro la dimensión de un arreglo bidimensional N x N
    y retorna una matriz con unos en los bordes y ceros en el centro.
    '''
    arreglo_unos = np.ones((10,10))
    arreglo_unos[1 : -1, 1 : -1] = 0

    return arreglo_unos 

print(unos_borde_ceros_centro(10))
