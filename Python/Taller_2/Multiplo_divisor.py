N = int(input('Ingrese el valor de n (un numero entero cualquiera):\n'))
M = int(input('Ingrese el valor de m (un numero entero cualquiera):\n'))

if M % N == 0:
    print(f'{N} es múltiplo y divisor de {M}.')
else:
    print(f'{N} no es ni múltiplo ni divisor de {M}.')