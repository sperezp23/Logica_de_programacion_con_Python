# Librerías
import numpy as np
import matplotlib.pyplot as plt

def ecuaciones_cinematicas(t, x0: float, y0: float, v0x: float, v0y: float) -> tuple:
    '''
    Recibe como parámetro las condiciones iniciales de movimiento de una partícula y 
    retorna una tupla conformada por dos arreglos con los datos su posición vertical y 
    horizontal.
    '''
    x = x0 + (v0x * t)
    y = x0 + (v0y * t) + (0.5 * g * (t ** 2))

    return x, y

def graficar_subplot(axs_x: float, axs_y: float, x, y, titulo: str) -> None:
    '''
    Recibe como parámetro, los indices del subplot a realizar, los datos a graficar y 
    el título de la gracia. 
    '''
    axs[axs_x,axs_y].plot(x,y)
    axs[axs_x,axs_y].set_xlabel(r'$x(t)$')
    axs[axs_x,axs_y].set_ylabel(r'$y(t)$')
    axs[axs_x,axs_y].set_title(titulo)
    axs[axs_x,axs_y].grid()

# Campo gravitatorio
g = -9.8

# Vector de tiempo
incremento = 0.01
t = np.arange(0,8 + incremento, incremento)

# Variables cinemáticas
x0_a = 0; y0_a = 100; v0x_a = 0; v0y_a = 0
x0_b = 0; y0_b = 100; v0x_b = 1; v0y_b = 0
x0_c = 0; y0_c = 0; v0x_c = 0; v0y_c = 10
x0_d = 0; y0_d = 0; v0x_d = 1; v0y_d = 10

# Ecuaciones cinemáticas
x_a, y_a = ecuaciones_cinematicas(t, x0_a, y0_a, v0x_a, v0y_a)
x_b, y_b = ecuaciones_cinematicas(t, x0_b, y0_b, v0x_b, v0y_b)
x_c, y_c = ecuaciones_cinematicas(t, x0_c, y0_c, v0x_c, v0y_c)
x_d, y_d = ecuaciones_cinematicas(t, x0_d, y0_d, v0x_d, v0y_d)

# Subplots
fig, axs = plt.subplots(2, 2)

# Gráfica de la función
graficar_subplot(0, 0, x_a, y_a, r'$a$')
graficar_subplot(0, 1, x_b, y_b, r'$b$')
graficar_subplot(1, 0, x_c, y_c, r'$c$')
graficar_subplot(1, 1, x_d, y_d, r'$d$')

# Ajustes entre gráficas
plt.subplots_adjust(hspace=0.6, wspace = 0.5) 

# Imprimir las gráficas
plt.show()
