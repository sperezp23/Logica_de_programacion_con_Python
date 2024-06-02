import re

def contraseña_correcta(contraseña: str) -> bool:
    '''
    Recibe como entrada una contraseña, y verifica si está cumple con
    los requisitos mínimos de seguridad.
    '''
    
    largo = True if len(contraseña) >= 8 else False
    mayusculas = True if len(re.findall(r'[A-Z]+', contraseña)) > 0 else False
    minusculas = True if len(re.findall(r'[a-z]+', contraseña)) > 0 else False
    numeros = True if len(re.findall(r'\d+', contraseña)) > 0 else False

    return all([largo, mayusculas, minusculas, numeros])

print(contraseña_correcta('123456Ab'))
