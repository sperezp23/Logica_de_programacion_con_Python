asignaturas = []
asignaturas_aprobadas = []
asignaturas_reprobadas = []
nota = -1

texto_asignatura = '''
Elija una de las siguientes opciones:
    [1]: Añadir asignatura.
    [2]: Finalizar.
'''

while True: 
    # Entradas
    opcion_elegida = input(texto_asignatura)
    
    # Añadir asignatura
    if opcion_elegida == '1':
        # Entrada 
        nombre_asignatura = input('Nombre de la asignatura:\n').lower()

        # Se pide la entrada hasta que esté en el rango especificado
        while True:
            if 0 <= nota <=5:
                break
            else:
                nota = float(input('Ingrese la nota obtenida (debe ser un numero entre 0 y 5):\n'))

        # Registrar la nueva asignatura y su nota
        asignaturas.append({nombre_asignatura:round(nota,1)})

                # Asignaturas aprobadas
        if nota >= 3:
            asignaturas_aprobadas.append({nombre_asignatura:round(nota,1)})
        else:
            asignaturas_reprobadas.append({nombre_asignatura:round(nota,1)})

        # Receta la nota 
        nota = -1

    # Terminar
    elif opcion_elegida == '2':
        break

# Salidas
print(f'Asignaturas:\n{asignaturas}')
print(f'\nAsignaturas aprobadas:\n{asignaturas_aprobadas}')
print(f'\nAsignaturas reprobadas:\n{asignaturas_reprobadas}')