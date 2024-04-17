from random import randint   

numero_de_intentos = 5
numero_secreto = randint(0,100)

while numero_de_intentos > 0:

    print(f'\nIntentos restantes: [{numero_de_intentos}/5]')
    numero_usuario = int(input('Ingrese un numero entre 0 y 100:\n'))

    if (numero_usuario < 0) or (numero_usuario > 100):
        print(f'El valor ingresado se halla fuera de rango.')

    elif numero_usuario > numero_secreto:
        numero_de_intentos -= 1
        print(f'El numero ingresado, {numero_usuario}, es MAYOR que el numero secreto.')

    elif numero_usuario < numero_secreto:
        numero_de_intentos -= 1
        print(f'El numero ingresado, {numero_usuario}, es MENOR que el numero secreto.')

    else:
        print(f'¡Adivinaste! el numero es: {numero_secreto}')
        break

if numero_de_intentos <= 0:
    print(f'Perdiste, el numero es: {numero_secreto}')