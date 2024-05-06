# Librerías
from random import randint   

# Declaración de variables
numero_de_intentos = 5
numero_secreto = randint(0,100)

print('🧐 Adivina el numero secreto 🤔')

# Mientas que el numero de intentos sea mayor a 0...
while numero_de_intentos > 0:

    # Entradas
    print(f'\nIntentos restantes: [{numero_de_intentos}/5]')
    numero_usuario = int(input('Ingrese un numero entre 0 y 100:\n'))

    # Numero fuera de rango
    if (numero_usuario < 0) or (numero_usuario > 100):
        print(f'El valor ingresado se halla fuera de rango.')

    # Mayor que el numero secreto
    elif numero_usuario > numero_secreto:
        numero_de_intentos -= 1
        print(f'El numero ingresado, {numero_usuario}, es MAYOR que el numero secreto.')

    # Menor que el numero secreto
    elif numero_usuario < numero_secreto:
        numero_de_intentos -= 1
        print(f'El numero ingresado, {numero_usuario}, es MENOR que el numero secreto.')

    # Numero secreto
    else:
        print(f'¡Adivinaste! el numero es: {numero_secreto}')
        break

# Sin intentos restantes
if numero_de_intentos <= 0:
    print(f'Perdiste, el numero es: {numero_secreto}')