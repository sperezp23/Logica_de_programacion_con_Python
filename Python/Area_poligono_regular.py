from math import pi, tan

n = int(input('Ingrese el numero de lados del polígono:\n'))
s = float(input('Ingrese el valor del lado del polígono:\n'))

area = (n*s**2)/(4*tan(pi/n))

print(f'El area del polígono es igual a {area}')
