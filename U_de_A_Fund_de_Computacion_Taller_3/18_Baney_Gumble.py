# Librerías
import matplotlib.pyplot as plt
from random import uniform

# Variables de Barney
pasos = 100000
x0 = 0
y0 = 0
x_hebreo = [x0]
y_hebreo = [y0]

# Calculo de la trayectoria
for paso in range(1, pasos + 1):
    paso_dado_x = uniform(-1,1)
    paso_dado_y = uniform(-1, 1)
    x_hebreo.append(x_hebreo[paso - 1] + paso_dado_x)
    y_hebreo.append(y_hebreo[paso - 1] + paso_dado_y)

# Graficar la trayectoria
plt.plot(x_hebreo, y_hebreo, label = 'Barney 😵')
plt.plot(max(x_hebreo), max(y_hebreo), label = 'Casa', marker = '^')
plt.plot(0, 0, label = "Moe's", marker = 'o', color = 'r')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trayectoria del Hebreo')
plt.grid()
plt.legend()
plt.show()
