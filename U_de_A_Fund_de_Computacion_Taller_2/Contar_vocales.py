palabra = input('Ingrese una palabra:\n').lower()

contador = {vocal:0 for vocal in 'aeiou'}

usar_metodos = bool(int(input('¿Usar metodos de los string?\n[0]: No\n[1]: Sí\n')))

if not usar_metodos:
    for i in palabra:
        match i:
            case 'a':
                contador['a'] += 1
            case 'e':
                contador['e'] += 1
            case 'i':
                contador['i'] += 1
            case 'o':
                contador['o'] += 1
            case 'u':
                contador['u'] += 1
else:
    contador['a'] = palabra.count('a')
    contador['e'] = palabra.count('e')
    contador['i'] = palabra.count('i')
    contador['o'] = palabra.count('o')
    contador['u'] = palabra.count('u')

print(f'La palabra ingresada {palabra}, tiene el siguiente conteo de vocales:\n{contador}')
