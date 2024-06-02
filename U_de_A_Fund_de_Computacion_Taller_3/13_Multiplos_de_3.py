import numpy as np

def multiplos_de_tres(n: int):
    '''
    Toma como parámetro la dimensión de un arreglo unidimensional con n elementos enteros y retorna
    otro arreglo conformado por los multiplos de 3 presentes en el arreglo inicial.
    '''
    a = np.arange(n)
    return a[a % 3 == 0]     

print(multiplos_de_tres(100))
