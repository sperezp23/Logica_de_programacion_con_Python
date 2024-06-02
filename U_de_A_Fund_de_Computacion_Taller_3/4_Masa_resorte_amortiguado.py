# Librerías
import numpy as np
import matplotlib.pyplot as plt

# Declaración de variables cinemáticas
A = 0.3
gamma = 0.15 
k = 4
m = 9

# Vector de tiempo
incremento = 0.1
t = np.arange(0, 25 + incremento, incremento)

# Vector de posición
y = A * np.exp(-gamma * t) * np.cos(np.sqrt(k/m) * t)

# Gráfica de la función
plt.figure()
plt.plot(t,y)
plt.xlabel(r'$t$',size = 15)
plt.ylabel(r'$y(t)$')
plt.title('Gráfica_MAS')
plt.grid()
plt.show()
