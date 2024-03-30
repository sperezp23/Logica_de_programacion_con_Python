# %% Funcion

def encuentro(Px:float, Py:float, Vx:float, Vy:float, Px2:float, Py2:float, Vx2:float, Vy2:float) -> str:

  '''Para el desarrollo de este reto, se asume que los cuerpos a modelar
   seguirán trayectorias rectas sobre el plano xy.'''

  # Si los vectores de velocidad son paralelos, las trayecorias nunca se cruzan
  if (abs(Vx2) == abs(Vx)) and (abs(Vy2) == abs(Vy)):

    print('Nunca se encuentran')

  # Si los vectores no son paralelos, por la condiciones del problema, las trayectorias se deben cruzar en algun punto.
  else:
    # Calculo del tiempo de encuentro
    t = (Px2 - Px)/(Vx - Vx2)

    # Calculo de la posición de los cuerpos (Como se van a encontar, en ese punto comparte coordenadas)
    x = Px + Vx*t
    y = Py + Vy*t
    print(f'Tiempo de encuentro: {t}\nPunto de encuentro P(x,y): P({x},{y})')

#---------------------------------------------------------------------------------------------------------------------------

# %% Main    

'''
Este programa no cuenta con esntradas, los parametros deben ser modificados
sobre el mismo codigo, más especificamente en las secciones: Cuerpo A, Cuerpo B.
'''

# Cuerpo A
Px = 0; Py = 0 # P(Px,Py): Posición en x y posición en y 
Vx = 2; Vy = 3 # V(Vx,Vy): Velocidad en x y Velocidad en y

# Cuerpo B
Px2 = 5; Py2 = 5 # P(Px,Py): Posición en x y posición en y 
Vx2 = 1; Vy2 = 2 # V(Vx,Vy): Velocidad en x y Velocidad en y

# Calculos de posición y tiempo
encuentro(Px, Py, Vx, Vy, Px2, Py2, Vx2, Vy2)