texto_entradas = '''
Ingrese el tipo de usuario.
[1]: menores de 2 años.
[2]: niños de 3 a 12 años.
[3]: Los mayores de 65 años.
[4]: Publico general.
[enter]: salir\n'''

entrada = input(texto_entradas)

costo_total = 0
numero_clientes={
    '1':0,
    '2':0,
    '3':0,
    '4':0
}

while entrada != '':
    entrada = input(texto_entradas)

    match entrada:
        case '1':
            numero_clientes['1'] += 1
        case '2':
            costo_total += 14
            numero_clientes['2'] += 1
        case '3':
            costo_total += 18
            numero_clientes['3'] += 1
        case '4':
            costo_total += 23
            numero_clientes['4'] += 1
        case '':
            break

print(f'''Descripción:
Menores de dos años: ({numero_clientes[1]})x0\t ${numero_clientes[1]*0:.2f}
Niños de 10 a 12 años: ({numero_clientes[2]})x14\t ${numero_clientes[2]*14:.2f}
Mayores de 65 años: ({numero_clientes[3]})x18\t ${numero_clientes[3]*18:.2f}
Publico general: ({numero_clientes[4]})x23\t\t ${numero_clientes[4]*23:.2f}
{'-'*32}
Total a pagar:{'\t'*3}${costo_total:.2f}''')
