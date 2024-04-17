n = int(input('Ingrese un numero:\n'))

suma = 0

for i in range(1,n):
    if n % i == 0:
        suma += i

if suma == n:
    print(f'{n} es un numero perfecto')
    
else:
    print(f'{n} no es un numero perfecto')