# Librerías
import numpy as np
import matplotlib.pyplot as plt

# Declaración de variables
e_1 = 0
e_2 = 0.5
e_3 = 0.8

# Vector de tiempo
incremento = 0.01
theta = np.arange(0, 2*np.pi + incremento, incremento)

# Vector de posición (cartesiano)
y_1_cartesiano = 1/(1 + (e_1 * np.cos(theta)))
y_2_cartesiano = 1/(1 + (e_2 * np.cos(theta)))
y_3_cartesiano = 1/(1 + (e_3 * np.cos(theta)))

# Vector de posición (polar)
x_1_polar = np.cos(theta)/(1 + (e_1 * np.cos(theta)))
y_1_polar = np.sin(theta)/(1 + (e_1 * np.cos(theta)))

x_2_polar = np.cos(theta)/(1 + (e_2 * np.cos(theta)))
y_2_polar = np.sin(theta)/(1 + (e_2 * np.cos(theta)))

x_3_polar = np.cos(theta)/(1 + (e_3 * np.cos(theta)))
y_3_polar = np.sin(theta)/(1 + (e_3 * np.cos(theta)))

# Subplots
fig, axs = plt.subplots(2, 1)

# Gráficas cartesianas
axs[0].plot(theta,y_2_cartesiano)
axs[0].plot(theta,y_1_cartesiano)
axs[0].plot(theta,y_3_cartesiano)
axs[0].set_xlabel(r'$t$')
axs[0].set_ylabel(r'$y(t)$')
axs[0].set_title('Orbitas_Elípticas (Cartesianas)',)
axs[0].grid()

# Gráfica de las orbitas elípticas
axs[1].plot(x_1_polar,y_1_polar)
axs[1].plot(x_2_polar,y_2_polar)
axs[1].plot(x_3_polar,y_3_polar)
axs[1].set_xlabel(r'$t$')
axs[1].set_ylabel(r'$y(t)$')
axs[1].set_title('Orbitas_Elípticas (Polares)',)
axs[1].grid()

# Ajustes entre gráficas
plt.subplots_adjust(hspace=0.5)  
plt.show()