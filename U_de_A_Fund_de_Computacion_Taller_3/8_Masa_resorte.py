# Librerías
import numpy as np
import matplotlib.pyplot as plt

def graficar_subplot(axs_x: float, x, y, titulo: str, y_label: str) -> None:
    '''
    Recibe como parámetro, los indices del subplot a realizar, los datos a graficar, 
    el título de la gracia y, titulo del eje y. 
    '''
    axs[axs_x].plot(x,y)
    axs[axs_x].set_xlabel(r'$t$')
    axs[axs_x].set_ylabel(y_label)
    axs[axs_x].set_title(titulo)
    axs[axs_x].grid()

# Declaración de variables cinemáticas
omega = 5
A = 1
k = 1
m = 1

# Vector de tiempo
incremento = 0.001
t = np.arange(0,8 + incremento, incremento)

# Ecuaciones cinemáticas
x = A * np.cos(omega * t)
v = -A * omega * np.sin(omega * t)
a = -A * (omega ** 2) * np.cos(omega * t)

# Ecuaciones energéticas
Ep = 0.5 * k * (x ** 2)
Ek = 0.5 * m * (v ** 2)

# Subplots 1
fig, axs = plt.subplots(3, 1)

# Gráfica de las ecuaciones cinemáticas
graficar_subplot(0, t, x, r'$Posición$', r'$x(t)$')
graficar_subplot(1, t, v, r'$Velocidad$', r'$v(t)$')
graficar_subplot(2, t, a, r'$Aceleración$', r'$a(t)$')

# Ajustes entre subplots
plt.subplots_adjust(hspace = 1) 

# Subplots 2
fig, axs = plt.subplots(2, 1)

# Gráficas de las ecuaciones energética
graficar_subplot(0, t, Ep, 'Energía potencial', r'$E_{p}(t)$')
graficar_subplot(1, t, Ek, 'Energía cinética', r'$E_{k}(t)$')

# Ajustes entre subplots
plt.subplots_adjust(hspace = 0.5) 

# Imprimir las gráficas
plt.show()
