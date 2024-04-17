asignaturas = {}
asignaturas_con_a = {} 
asignaturas_aprobadas = {} 
asignaturas_reprobadas = {} 
nota = -1

while True:
    opcion_elegida = input('''
Elija una de las siguientes opciones:
    [1]: Añadir asignatura.
    [2]: Finalizar.
''')

    if opcion_elegida == '1':
        asignatura = input('Ingrese el nombre de la asignatura:\n').lower()
    
        while True:
            if 0 <= nota <=5:
                break
            else:
                nota = float(input('Ingrese la nota de la asignatura (debe ser un numero entre 0 y 5):\n'))
        
        asignaturas[asignatura] = nota

        if 'a' in asignatura:
            asignaturas_con_a[asignatura] = nota

        if nota >= 3:
            asignaturas_aprobadas[asignatura] = nota
        else:
            asignaturas_reprobadas[asignatura] = nota
        
        nota = -1
    
    elif opcion_elegida == '2':
        break

print(f'Asignaturas:\n{asignaturas}')
print(f'\nAsignaturas con a:\n{asignaturas_con_a}')
print(f'\nAsignaturas aprobadas:\n{asignaturas_aprobadas}')
print(f'\nAsignaturas reprobadas:\n{asignaturas_reprobadas}')