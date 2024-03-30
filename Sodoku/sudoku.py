# pylint: disable=missing-docstring

def sudoku_validator(grid):

    contador = 0
    correcto = True
    mensaje= f'Sudoku correcto?\n{correcto}'

    for i in range(0,9,3):

        a = grid[i][i:i+3]+grid[i+1][i:i+3]+grid[i+2][i:i+3]

        for j in range(1,10):
            
            if a.count(j) > 1:
                correcto = False
                mensaje = f'Sudoku correcto?\n{correcto}' 
                break

    if correcto:

        for i in range(0,9):

            for j in range(1,10):

                if (grid[i].count(j) > 1) or (contador > 9):
                    correcto = False
                    mensaje = f'Sudoku correcto?\n{correcto}'
                    break

                else:
                    contador += grid[i].count(j)

            contador = 0

    if correcto:

        for i in range(0,9):

            columnas = []

            for j in range(0,9):

                columnas.append(grid3[i][j])

            columnas.sort()

            if not(list(set(columnas)) == columnas):
                correcto = False
                mensaje= f'Sudoku correcto?\n{correcto}' 
                break 

    return mensaje

grid1 = [
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
grid2 = [
    [8,8,4,  1,5,9,  2,2,6],
    [5,2,9,  6,8,2,  8,4,1],
    [6,1,2,  4,2,8,  8,5,9],

    [9,2,8,  8,1,5,  4,6,2],
    [2,5,8,  8,4,6,  1,9,2],
    [4,6,1,  9,2,2,  5,8,8],

    [8,8,6,  2,9,4,  2,1,5],
    [2,4,2,  5,6,1,  9,8,8],
    [1,9,5,  2,8,8,  6,2,4]
]
grid3 = [
    [1,2,3, 4,5,6, 7,8,9],
    [2,3,1, 5,6,4, 8,9,7],
    [3,1,2, 6,4,5, 9,7,8],

    [4,5,6, 7,8,9, 1,2,3],
    [5,6,4, 8,9,7, 2,3,1],
    [6,4,5, 9,7,8, 3,1,2],

    [7,8,9, 1,2,3, 4,5,6],
    [8,9,7, 2,3,1, 5,6,4],
    [9,7,8, 3,1,2, 6,4,5]
]
grid4 = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,2,7,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]

print('\n'+sudoku_validator(grid1))
print(sudoku_validator(grid2))
print(sudoku_validator(grid3))
print(sudoku_validator(grid4)+'\n')