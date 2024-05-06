resistencias = list(map(float,input('Ingrese 3 valores separados por "," (coma):\n').split(',')))[0:3]
configuracion = input('Ingrese 1:Serie o 2:Paralelo según el tipo de configuración.\n')

configuraciones = {
    '1':'serie',
    '2':'paralelo'
}

if configuraciones[configuracion] == configuraciones['1']:
    resistencia_total = sum(resistencias)
    
else:
    resistencia_total = 1/sum(map(lambda resistencia :1/resistencia, resistencias))

print(f'Para una configuración en {configuraciones[configuracion]}, el valor de la resistencia total es: {resistencia_total}')