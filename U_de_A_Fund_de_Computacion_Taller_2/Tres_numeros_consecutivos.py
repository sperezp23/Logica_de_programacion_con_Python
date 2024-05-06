# entrada = [1,  1,  1,  64,  23,  64,  22,  22,  22]
entrada = [1,  1,  1,  3,  3,  3,  22,  22,  22]
salida = []

for indice in range(1,len(entrada)-1):
    if entrada[indice-1] == entrada[indice] == entrada[indice+1]:
        salida.append(entrada[indice])

print(salida)
