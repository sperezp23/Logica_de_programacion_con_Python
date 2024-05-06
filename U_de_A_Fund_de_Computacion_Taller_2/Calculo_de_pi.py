N = float(input('Ingrese el valor de N:\n'))

suma = 0

for n in range(0,int(N)+1):
    suma += ((-1)**n)/(2*n+1)

print(f'Valor aproximado de pi para N = {N}\npi = {4*suma}') 
