# Entrada
# sudoku = [
#     [7,8,4,  1,5,9,  3,2,6],
#     [5,3,9,  6,7,2,  8,4,1],
#     [6,1,2,  4,3,8,  7,5,9],

#     [9,2,8,  7,1,5,  4,6,3],
#     [3,5,7,  8,4,6,  1,9,2],
#     [4,6,1,  9,2,3,  5,8,7],

#     [8,7,6,  3,9,4,  2,1,5],
#     [2,4,3,  5,6,1,  9,7,8],
#     [1,9,5,  2,8,7,  6,3,4]
# ]

# sudoku = [
#     [7j,8j,4j,  1j,5j,9j,  3j,2j,6j],
#     [5j,3j,9j,  6j,7j,2j,  8j,4j,1j],
#     [6j,1j,2j,  4j,3j,8j,  7j,5j,9j],

#     [9j,2j,8j,  7j,1j,5j,  4j,6j,3j],
#     [3j,5j,7j,  8j,4j,6j,  1j,9j,2j],
#     [4j,6j,1j,  9j,2j,3j,  5j,8j,7j],

#     [8j,7j,6j,  3j,9j,4j,  2j,1j,5j],
#     [2j,4j,3j,  5j,6j,1j,  9j,7j,8j],
#     [1j,9j,5j,  2j,8j,7j,  6j,3j,4j]
# ]

# Sudoku Ismael
sudoku = [
    [9,1,4, 6,2,7, 3,8,5],
    [6,3,7, 9,5,8, 4,1,2],
    [2,8,5, 4,3,1, 9,6,7],

    [4,5,3, 1,7,9, 8,2,6],
    [1,2,8, 5,6,3, 7,4,9],
    [7,9,6, 2,8,4, 1,5,3],

    [8,6,9, 7,1,5, 2,3,4],
    [3,4,2, 8,9,6, 5,7,1],
    [5,7,1, 3,4,2, 6,9,8]
 ]

# Declaración de variables
correcto = True
contador = {digito:0 for digito in range(1,10)}
contador_filas = 0

# Comprobar cuadros 3x3
for fila in range(0,9,3):
    cuadrado = sudoku[fila][fila:fila+3]+sudoku[fila+1][fila:fila+3]+sudoku[fila+2][fila:fila+3]

    for i in range(len(cuadrado)):
        numero = abs(cuadrado[i])
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
            contador[abs(numero)] += 1

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
            numero = abs(sudoku[fila][columna])
            contador[numero] += 1

            if 2 in contador.values():
                correcto = False
                print(f'La columna {columna} tiene más de un {numero}.')
                break
        
        contador = {digito:0 for digito in range(1,10)}

# Si todo está correcto...               
if correcto:
    print('😮 La matriz ingresada es un Sudoku. 🧐')
    