from numpy import *
from matplotlib.pyplot import *


"""
datos = loadtxt("/datos.dat")

print(datos,'\n')
print(datos[0],'\n')
print(datos[0:2],'\n')
print(datos[:,1],'\n')
print(datos[0,:],'\n')

datos=loadtxt("/datos.dat",usecols=(1,2))
"""

datos=loadtxt('AM2229-735_sat_VLR_ext_8_1_016_006.txt', usecols=(1,2,3))

print(datos)

x=datos[:,0]
y=datos[:,1]
z=datos[:,2]

print(x)
show()

plot(x,z,".")

# ajustando las proporciones de los ejes

# tamaño del lienzo
figure(figsize=(5,5))
plot(x,z,".")
show()