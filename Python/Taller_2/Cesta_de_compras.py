lista_compras = {}
continuar = True
tres_puntos = '.'*3

while continuar:
    articulo, precio = input('Ingrese el nombre del articulo y el precio del producto separados por ","(Articulo, precio):\n').split(',')

    continuar = bool(int(input('''¿Desea agregar otro artículo?
    [1] Continuar.
    [0] Terminar.\n''')))

    lista_compras[articulo] = float(precio)

for articulo, precio in lista_compras.items():
    print(f'{articulo}\t{precio}')

print(f'{tres_puntos}\t{tres_puntos}\nTotal\t{sum(lista_compras.values())}')
