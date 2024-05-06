from functools import cache

@cache
def fact(n:float) -> float:
    '''
    Calcula el factorial del numero que recibe como parámetro.
    '''

    if n == 0:
        return 1
    
    else:
        return n*fact(n-1)