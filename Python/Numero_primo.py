esPrimo = True
primos_menores_de_8 = [2,3,5,7]

n = int(input('Ingrese un numero:\n'))
raiz_de_n = int((n)**0.5)+1

if n < 8: 
    if n not in primos_menores_de_8:
        esPrimo = False

    elif n in primos_menores_de_8:
        esPrimo = True

else:
    for i in range(2,raiz_de_n):
        if n % i == 0:
            esPrimo = False

if esPrimo:
    print(f'El numero ingresado, {n}, es primo.')
else:
    print(f'El numero ingresado, {n}, es no primo.')