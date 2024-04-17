# entrada = [1, 2, 5, 2, 4, 5, 7, 2]
entrada = [2,3,4,6]
salida = []

for indice in range(1,len(entrada)):
    salida.append(max(entrada[indice-1],entrada[indice]))

print(salida)