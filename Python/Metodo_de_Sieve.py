n = int(input('Ingrese el numero de primos que desea imprimir:\n'))

vector_unos = [1]*n
vector_primos = []

for i in range(1,n):
    for j in range(2,n):
        if ((i+1) >= j**2) and ((i+1) % j == 0):
            vector_unos[i] = 0

    if vector_unos[i] == 1:
        vector_primos.append(i+1)

print(vector_primos)
