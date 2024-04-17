n = int(input('Ingrese el valor de N:\n'))

numeros = range(1,n+1)
suma = 0

for i in numeros:
    suma += i

print(f'''Suma de los primeros N enteros.
Por formula: {(n*(n+1))/2:n}
Función suma directa: {sum(numeros)}
Suma con ciclos: {suma}''')
