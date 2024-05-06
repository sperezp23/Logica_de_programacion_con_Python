from funcion_factorial import fact

N = float(input('Ingrese el valor de N:\n'))
x = float(input('Ingrese el valor de x:\n'))

suma = 0
factorial = 1.0

for n in range(0,int(N)+1):
    suma += ((-1)**n)*(x**(2*n))/(fact(2*n))

print(f'Resultado con funciones(recurrencia): {suma}')

suma = 0

for n in range(0,int(N)+1):
    n_factorial = 2*n

    while n_factorial > 1:
        factorial *= n_factorial
        n_factorial = n_factorial - 1

    suma += ((-1)**n)*(x**(2*n))/(factorial)
    
print(f'Resultado con ciclos: {suma}')
