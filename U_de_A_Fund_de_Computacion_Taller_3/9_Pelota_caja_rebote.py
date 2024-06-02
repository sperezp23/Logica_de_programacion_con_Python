# Librerías
import matplotlib.pyplot as plt

# Tiempo de simulación
tiempo_max = 350
dt = 0.1

# Declaración de variables
lado_caja = 10

# Inicializar posición y velocidad de la pelota
x = 0; v0x = 2
y = 0; v0y = 3

# Listas para almacenar la trayectoria
trayectoria_x = [x]
trayectoria_y = [y]

for t in range(int(tiempo_max / dt)):
    # Actualizar posición de la pelota
    x += v0x * dt
    y += v0y * dt

    # Rebotar en las paredes
    if x <= 0 or x >= lado_caja:
        v0x = -v0x

    if y <= 0 or y >= lado_caja:
        v0y = -v0y

    # Almacenar la trayectoria
    trayectoria_x.append(x)
    trayectoria_y.append(y)

# Graficar la trayectoria
plt.plot(trayectoria_x, trayectoria_y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trayectoria de la pelota en la caja')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
