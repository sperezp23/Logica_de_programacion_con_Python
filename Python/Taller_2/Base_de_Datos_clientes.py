db_clientes = {
    '0':{
        'nombre':'Goku',
        'direccion':'Came House',
        'telefono':1618,
        'correo':'Goku_God@Kmail.com',
        'preferente':True
    },

    '1':{
        'nombre':'Goku',
        'direccion':'Capsula Corp',
        'telefono':3141,
        'correo':'Krilin_God@Capsulamail.com',
        'preferente':False
    }
}

while True:
    opcion_elegida = input('''
Elija una de las siguientes opciones:
    [1]: Añadir cliente.
    [2]: Eliminar cliente.
    [3]: Mostrar cliente.
    [4]: Listar todos los clientes.
    [5]: Listar clientes preferentes.
    [6]: Terminar.
''')

    # Añadir cliente
    if opcion_elegida == '1':
        id_cliente = input('Ingrese el ID del nuevo cliente:\n')

        db_clientes[id_cliente]={
            'nombre':input('Ingrese el Nombre del nuevo cliente:\n'),
            'direccion':input('Ingrese la dirección del nuevo cliente:\n'),
            'telefono':int(input('Ingrese el teléfono del nuevo cliente:\n')),
            'correo':input('Ingrese el Correo del nuevo cliente:\n'),
            'preferente':bool(int(input('¿Cliente preferente?:\n[0]: No.\n[1]: Sí.\n')))
        }

        print(f'\nEl cliente id:{id_cliente} a sido agregado con éxito.')

    # Eliminar cliente
    elif opcion_elegida == '2':
        id_cliente = input('Ingrese el ID del cliente que desea eliminar:\n')

        if id_cliente not in db_clientes.keys():
            print('El cliente no se encuentra registrado.')
        
        else:
            del(db_clientes[id_cliente])

            print(f'\nEl cliente id:{id_cliente} a sido eliminado.')

    # Mostrar cliente
    elif opcion_elegida == '3':
        id_cliente = input('Ingrese el ID del cliente que desea mostrar:\n')

        if id_cliente not in db_clientes.keys():
            print('El cliente no se encuentra registrado')
        else:
            print(db_clientes[id_cliente])

    # Listar todos los clientes
    elif opcion_elegida == '4':
        if len(db_clientes) == 0:
            print('No hay clientes registrados')
        else:
            print(db_clientes)

    # Listar clientes preferences
    elif opcion_elegida == '5':
        clientes_preferentes = []
        
        for cliente in db_clientes.keys():
            if db_clientes[cliente]['preferente']:
                clientes_preferentes.append(db_clientes[cliente])

        if len(clientes_preferentes) == 0:
            print('No hay clientes preferentes.')
        else:
            print(clientes_preferentes)

    # Terminar
    elif opcion_elegida == '6':
        break
