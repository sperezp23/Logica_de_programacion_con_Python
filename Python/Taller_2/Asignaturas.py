# Declaración de variables
asignaturas = {}
asignaturas_con_a = {} 
asignaturas_aprobadas = {} 
asignaturas_reprobadas = {} 
nota = -1

# Ciclo infinito
while True:

    # Entradas
    opcion_elegida = input('''
Elija una de las siguientes opciones:
    [1]: Añadir asignatura.
    [2]: Finalizar.
''')

    # Añadir asignatura
    if opcion_elegida == '1':

        # Entrada 
        asignatura = input('Ingrese el nombre de la asignatura:\n').lower()
    
        # Se pide la entrada hasta que esté en el rango especificado
        while True:
            if 0 <= nota <=5:
                break
            else:
                nota = float(input('Ingrese la nota de la asignatura (debe ser un numero entre 0 y 5):\n'))
        
        # Registrar la nueva asignatura y su nota
        asignaturas[asignatura] = nota

        # Asignaturas con a
        if 'a' in asignatura:
            asignaturas_con_a[asignatura] = nota

        # Asignaturas aprobadas
        if nota >= 3:
            asignaturas_aprobadas[asignatura] = nota
        else:
            asignaturas_reprobadas[asignatura] = nota
        
        # Receta la nota 
        nota = -1
    
    # Terminar
    elif opcion_elegida == '2':
        break

# Salidas
print(f'Asignaturas:\n{asignaturas}')
print(f'\nAsignaturas con a:\n{asignaturas_con_a}')
print(f'\nAsignaturas aprobadas:\n{asignaturas_aprobadas}')
print(f'\nAsignaturas reprobadas:\n{asignaturas_reprobadas}')