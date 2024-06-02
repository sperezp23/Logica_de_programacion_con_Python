# Librerías
import math as m
import numpy as np
import pandas as pd

def evaluar_funcion(paso: float) -> None:
    '''
    Recibe el paso con el cual se evaluará la función f(x) = sin(x) * Ln(x+1) * sinh(x) al
    interior del intervalo [0,10].
    '''

    usar_pandas = bool(int(input('''¿Con cual librería dese generar el archivo CSV con los datos generados?
[0]: Numpy
[1]: Pandas''')))
    
    datos = []
    index = 1

    for x in range(0,10 + paso, paso):
        f = m.sin(x) * m.log(x + 1) * m.sinh(x)

        datos.append([index, x, f])
        index += 1    

        if x == 10: 
            print('Archivo creado.')

    if usar_pandas:
        df = pd.DataFrame(datos,columns=['Iteración', 'x', 'f(x)'])
        df.to_csv('Datos.csv', index=False)

    else: 
        np.savetxt('Datos.csv', np.array(datos), delimiter=',')

evaluar_funcion(1)
