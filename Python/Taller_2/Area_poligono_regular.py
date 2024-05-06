# Librerías
from math import pi, tan

# Entradas
n = int(input('Ingrese el numero de lados del polígono:\n'))
s = float(input('Ingrese el valor del lado del polígono:\n'))

# Calculo del área
area = (n*s**2)/(4*tan(pi/n))

# Salida
print(f'El area del polígono es igual a {area}')
