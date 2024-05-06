peso = float(input('Ingrese el valor de su peso en [Kg]:\n'))
estatura = float(input('Ingrese el valor de su estatura en [m]:\n'))

imc = peso/(estatura**2)

if imc < 18.5:
    print(f'Su imc tiene un valor de: {imc:.4f}\n Usted tiene peso bajo.')

elif 18.5 <= imc < 24.9:
    print(f'Su imc tiene un valor de: {imc:.4f}\n Usted tiene peso normal.')

elif 25 <= imc <= 29.9:
    print(f'Su imc tiene un valor de: {imc:.4f}\n Usted tiene sobrepeso.')
    
elif imc > 30:
    print(f'Su imc tiene un valor de: {imc:.4f}\n Usted tiene obesidad.')
