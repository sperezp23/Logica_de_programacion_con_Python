def palabras_frecuencias(lista_palabras: list[str]) -> dict:
    '''
    Recibe una lista de palabras y retorna un diccionario con la frecuencia 
    de registro de cada palabra. 
    '''

    return {palabra : lista_palabras.count(palabra) for palabra in lista_palabras}

def palabra_mas_repetida(frecuencias_dict: dict[str,int]) -> tuple:
    '''
    Recibe un diccionario que contiene palabras así como su frecuencia de registro y
    retorna una tupla con la palabra más repetida junto con su frecuencia.
    '''
    
    max_frecuencia = -1

    for palabra,frecuencia in frecuencias_dict.items():
        if frecuencia > max_frecuencia:
            palabra_mas_larga = palabra
            max_frecuencia = frecuencia

    return palabra_mas_larga, max_frecuencia

frecuencias_dict = palabras_frecuencias(['a', 'c', 'aa', 'aaa','a'])
print(palabra_mas_repetida(frecuencias_dict))
