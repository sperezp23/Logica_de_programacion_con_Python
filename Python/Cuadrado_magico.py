
# Otros cuadrados mágicos: 
# https://blogs.elespectador.com/actualidad/ecuaciones-de-opinion/cuadrado-magico-ramanujan
# https://blogsaverroes.juntadeandalucia.es/recursosdematematicas/cuadrado-magico-aditivo-de-orden-9/

# Entradas
# cuadrado_magico = [
#     [4, 9, 2],
#     [3, 5, 7],
#     [8, 1, 6]
# ]

# Cuadrado magico de Ramanuja
# cuadrado_magico = [
#     [22, 12, 18, 87],
#     [88, 17, 9, 25],
#     [10, 24, 89, 16],
#     [19, 86, 23, 11]
# ]

# Cuadrado magico sagrada familia
cuadrado_magico = [
    [1, 14, 14, 4],
    [11, 7, 6, 9],
    [8, 10, 10, 5],
    [13, 2, 3, 15]
]

dimension = len(cuadrado_magico[0])

# Guardar sumas
sum_filas = []
sum_columnas = []
suma_columnas_acumulador = 0
sum_diagonal_prin = 0
sum_diagonal_sec = 0

# ¿Correcto?
correcto = True

# Suma de las filas
for fila in range(dimension):
    sum_diagonal_sec += cuadrado_magico[fila][(dimension-1)-fila]
    sum_filas.append(sum(cuadrado_magico[fila]))

    # Verificar la suma de las filas
    if (fila >= 1) and (sum_filas[fila-1] != sum_filas[fila]):
        print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la fila {fila} no coincide con la suma de la fila {fila-1}.')
        correcto = False
        break

# Verificar suma de la diagonal secundaria con las suma de las filas
if (sum_diagonal_sec not in sum_filas) and correcto:
    print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la diagonal secundaria no coincide con la suma de las filas.')
    correcto = False

if correcto:
    # Suma de las columnas(Transpuesta de la matriz)
    for columna in range(dimension):
        for fila in range(dimension):
            suma_columnas_acumulador += cuadrado_magico[fila][columna]

            # Suma de la diagonal principal
            if columna == fila:
                sum_diagonal_prin += cuadrado_magico[fila][columna]

        sum_columnas.append(suma_columnas_acumulador)
        suma_columnas_acumulador = 0

        # Verificar la suma de las columnas
        if (columna >= 1) and (sum_columnas[columna-1] != sum_columnas[columna]):
            print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la columna {columna} no coincide con la suma de la columna {columna-1}.')
            correcto = False
            break

    # Verificar la suma de la diagonal principal contra las filas
    if (sum_diagonal_prin not in sum_filas) and correcto:
        print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la diagonal principal no coincide con la suma de las filas.')
        correcto = False

    # Verificar la suma de la diagonal principal contra las columnas
    elif (sum_diagonal_prin not in sum_columnas) and correcto:
        print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la diagonal principal no coincide con la suma de las columnas.')
        correcto = False

    # Verificar la suma de la diagonal secundaria contra las columnas
    elif (sum_diagonal_sec not in sum_columnas) and correcto:
        print(f'La matriz ingresada NO es un cuadrado mágico.\nLa suma de la diagonal secundaria no coincide con la suma de las columnas.')

    # Cuadrado Perfecto
    else:
        print(f'''😱 La matriz ingresada es un cuadrado mágico.🥳
    Sumas de las filas: {sum_filas}
    Sumas de las columnas: {sum_columnas}
    Sumas de la diagonal principal: {sum_diagonal_prin}
    Sumas de la diagonal secundaria: {sum_diagonal_sec}''')
        
