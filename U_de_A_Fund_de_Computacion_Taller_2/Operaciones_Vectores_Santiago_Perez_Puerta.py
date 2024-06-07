vector_resultado = []
resultado_numerico = 0

texto_entradas = '''
¿Que operación desea realizar entre los vectores?:
    [1]: Sumarlos.
    [2]: Restarlos.
    [3]: Producto Punto.
    [4]: Producto Cruz.
    [5]: Terminar
'''

while(True):
    vector_1 = list(map(float,input('\nIngrese las tres componentes del vector 1 separadas por ",":\n').split(',')))[0:3]
    
    vector_2 = list(map(float,input('Ingrese las tres componentes del vector 2 separadas por ",":\n').split(',')))[0:3]

    while True:
        operacion = input(texto_entradas)


        if (operacion in '12345') and (operacion !=''):
            break
        else: 
            print(f'{'⚠ '*3} Operación no válida {'⚠ '*3}\n{'-'*35}')

    # Sumarlos
    if operacion =='1':
        vector_resultado = [round(vector_1[i] + vector_2[i],2) for i in range(len(vector_1))]
        
        print(f'Suma resultante: {vector_resultado}')

    # Restarlos
    if operacion =='2':
        vector_resultado = [round(vector_1[i] - vector_2[i],2) for i in range(len(vector_1))]
        
        print(f'Resta resultante: {vector_resultado}')

    # Producto Punto
    if operacion =='3':
        resultado_numerico = vector_1[0]*vector_2[0]+vector_1[1]*vector_2[1]+vector_1[2]*vector_2[2]
        
        print(f'Numero resultante: {resultado_numerico:.2f}')

    # Producto Cruz
    if operacion =='4':
        vector_resultado = [round(vector_1[1]*vector_2[2]-vector_2[1]*vector_1[2],2),
                            round(-vector_1[0]*vector_2[2]-vector_2[0]*vector_1[2],2),
                            round(vector_1[0]*vector_2[1]-vector_2[0]*vector_1[1],2)]
        
        print(f'Vector resultante: {vector_resultado}')

    # Terminar
    if operacion =='5':
        break  
