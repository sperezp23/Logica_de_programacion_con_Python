import numpy as np

n = int(input("Ingrese el valor de n:\n"))
a = list(map(int,input("\nIngrese el valor de los dos pares de coordenadas (x,y), separadas por espacio:\n").strip().split()))

PuntosX = []
PuntosY = []

#Variables auxiliares para voltear los puntos y los recorridos
aux = 1
aux1 = 1

#Para no reecribir todo el codigó y tener que implementar toda una nueva 
#logica se aprovecha el hecho de que no importa el sentido del recorrido la distancia 
#es la misma y por lo tanto, se puede cambiar el orden de los puntos y el resultado  
#será el mismo

if (a[2]- a[0])<0 or (a[3] - a[1]) < 0: #Pregunta cual puto está más lejos del otro,
 #en caso de que se deba retrocesder y no avanzar
  aux = a[0] 
  a[0]= a[2]
  a[2]=aux

  aux1=a[1]
  a[1]=a[3]
  a[3]=aux1

  aux = -1
  aux1 = 1

mat = np.ones((n,n)) #Matriz para verificar que el progrma funciona.
 
deltaX = abs(a[2] - a[0]) #Distancia entre puntos
deltaY = abs(a[3] - a[1])#Distancia entre puntos
costo = deltaX + deltaY -1#Costo requerído en el problema, descontando el punto de llegada

#Desplazamiento en X (Horizontal)
for i in range(1,deltaX+1):
  PuntosX.append((a[0]+i,a[1]))

#Segenera una lista de tuplas para representar las  coordenadas
#Se le suma del desplazamineto al punto inicial para generar el recorrido

#Desplazamiento en Y (Vertical)
if deltaX != 0:
  for i in range(1,deltaY):
    PuntosY.append((PuntosX[-1][0],a[1]+i))
#Si hay desplazamiento en X, se debe desplazar en Y 
#apartir del ultimo punto horizontal obtenido 
else:
  for i in range(1,deltaY+1):
    PuntosY.append((a[0],a[1]+i))
#Sino hay desplazamiento en X, se procede a generar los puntos de Y desde el punto inicial

#Ya que se necesitan los puntos de llegada para que el codigo anterior funcione,
#aquí se eliminan para otorgar la salida esperada.
if deltaX == 0:
  del(PuntosY[-1])
elif deltaY == 0:
  del(PuntosX[-1])

#Se almacenan los recorridos de X y Y en un vector final que será el recorrido completo.
Recorrido = PuntosX+PuntosY

# print("Puntos ingresados: {0}".format(a))
# print("DeltaX = {0}".format(deltaX))
# print("DeltaY = {0}".format(deltaY))
# print("PuntosX: {0}".format(PuntosX))
# print("PuntosY: {0}".format(PuntosY))

#Traza el recorrido de en la matriz
for i in Recorrido:
    mat[i]= 0

#Se imprimen la salida esperada
print(mat) #Matriz de problema
print("Costo = {0}".format(costo))
print("Recorrido: {0}".format(Recorrido[::aux][::aux1]))
#Con ayuda de las variavles aux y aux1, se voltea el recorrido en caso de que se 
#halla retrocedido en lugar de avanzar.