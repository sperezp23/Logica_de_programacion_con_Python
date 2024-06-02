def palabra_mas_larga(lista_palabras : list[str]) -> tuple:
    '''
    Recibe por parámetro una lista de palabras y retorna
    una tupla con la palabra más larga y su longitud. 
    '''
    max_largo_palabra = -1

    for palabra in lista_palabras:
        largo_palabra = len(palabra)

        if largo_palabra > max_largo_palabra:
            palabra_mas_larga = palabra
            max_largo_palabra = largo_palabra

    return palabra_mas_larga, max_largo_palabra

print(palabra_mas_larga(['a', 'aaa', 'b']))
