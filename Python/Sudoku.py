# Entrada
sudoku = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]

# Declaración de variables
correcto = True
contador = {digito:0 for digito in range(1,10)}
contador_filas = 0

# Comprobar cuadros 3x3
for fila in range(0,9,3):
    cuadrado = sudoku[fila][fila:fila+3]+sudoku[fila+1][fila:fila+3]+sudoku[fila+2][fila:fila+3]

    for i in range(len(cuadrado)):
        numero = cuadrado[i]
        contador[numero] += 1

        if 2 in contador.values():
            correcto = False
            print(f'El bloque {fila} tiene más de un {numero}.')
            break
    
    contador = {digito:0 for digito in range(1,10)}

# Comprobar Filas
if correcto:
    for fila in sudoku:
        for numero in fila:
            contador[numero] += 1

            if 2 in contador.values():
                correcto = False
                print(f'La fila {contador_filas} tiene más de un {numero}.')
                break
        
        contador_filas += 1
        contador = {digito:0 for digito in range(1,10)}

# Comprobar Columnas
if correcto:
    for columna in range(0,9):
        for fila in range(0,9):
            numero = sudoku[fila][columna]
            contador[numero] += 1

            if 2 in contador.values():
                correcto = False
                print(f'La columna {columna} tiene más de un {numero}.')
                break
        
        contador = {digito:0 for digito in range(1,10)}

# Si todo está correcto...               
if correcto:
    print('😮 La matriz ingresada es un Sudoku. 🧐')
    