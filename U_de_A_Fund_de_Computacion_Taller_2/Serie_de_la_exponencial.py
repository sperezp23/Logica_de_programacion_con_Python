from funcion_factorial import fact

N = float(input('Ingrese el valor de N:\n'))
x = float(input('Ingrese el valor de x:\n'))

suma = 0
factorial = 1.0

for n in range(0,int(N)+1):
    suma += (x**n)/(fact(n))

print(f'Resultado con funciones(recurrencia): {suma}')

suma = 0

for n in range(0,int(N)+1):

    while n > 1.0:
        factorial *= n
        n = n - 1.0

    suma += (x**n)/(factorial)
    
print(f'Resultado con ciclos: {suma}')
