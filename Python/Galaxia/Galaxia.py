import numpy as np
import matplotlib.pyplot as plt
from time import sleep

datos = np.loadtxt('AM2229-735_sat_VLR_ext_8_1_016_006.txt', usecols=(1,2,3))

# print(datos)

x=datos[:,0]
y=datos[:,1]
z=datos[:,2]

plt.figure(figsize=(5,5))
plt.plot(x,y,marker="*",color= 'b',linestyle='',label='Galaxia')
plt.xlabel(r"$\sin(x)=\frac{1}{2}$",size = 15)
plt.ylabel(r"$y$",size = 15, rotation = 0)

plt.figure(figsize=(5,5))
plt.plot(x,y,marker="*",color= 'r',linestyle='',label='Galaxia')
plt.xlabel(r"$\sin(x)=\frac{1}{2}$",size = 15)
plt.ylabel(r"$y$",size = 15, rotation = 0)

plt.figure(figsize=(5,5))
plt.plot(x,y,marker="*",color= '#0984f3',linestyle='',label='Galaxia')
plt.xlabel(r"$\sin(x)=\frac{1}{2}$",size = 15)
plt.ylabel(r"$y$",size = 15, rotation = 0)

plt.show()
