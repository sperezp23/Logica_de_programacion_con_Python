#Librerías
import json
import csv

# Variables 
temperatura_fenomenos_dict = {}
temperatura_fenomenos_csv = [['nombre','Temp_K','Temp_°C','Temp_°F']]

# Leer archivo
with open('temperaturas.txt','r') as archivo_temp:
  temperaturas_txt = archivo_temp.readlines()

# Leer archivo txt
for linea in temperaturas_txt:
  nombre, temperatura, unidad =linea.replace('\n', '').lower().split(',')

  temperatura = float(temperatura)

  # Conversión de unidades según sea el caso y, guardar en el diccionario para crear luego el Json
  match unidad:
    # si la temperatura está en K
    case 'k':
      temperatura_farenheit = round((temperatura * 9/5) + 459.67,4)
      temperatura_celsius = round(temperatura - 273.15,4)

      temperatura_fenomenos_dict[nombre] = {
        'celsius':temperatura_celsius,
        'farenheit':temperatura_farenheit,
        'kelvin':temperatura
      }
      
    # si la temperatura está en K
    case 'f':
      temperatura_kelvin = round((temperatura-32)/1.8 + 273.15, 4)
      temperatura_celsius = round((temperatura-32)/1.8, 4)

      temperatura_fenomenos_dict[nombre] = {
        'celsius':temperatura_celsius,
        'farenheit':temperatura,
        'kelvin':temperatura_kelvin
      }

    # si la temperatura está en K
    case 'c':
      temperatura_farenheit = round((temperatura * 1.8) + 32)
      temperatura_kelvin = round(temperatura + 273.15,4)

      temperatura_fenomenos_dict[nombre] = {
        'celsius':temperatura,
        'farenheit':temperatura_farenheit,
        'kelvin':temperatura_kelvin
      }

  # Guardar la lista de datos en otra lista para crear el cvs
  temperatura_fenomenos_csv.append([
    nombre,str(temperatura_fenomenos_dict[nombre]['kelvin'])+'K',
    str(temperatura_fenomenos_dict[nombre]['celsius'])+'°C',
    str(temperatura_fenomenos_dict[nombre]['farenheit'])+'°F'
    ])
        
# Abrir el archivo en modo escritura
with open('temperaturas.csv', 'w', newline='') as archivo_csv:
  escritor_csv = csv.writer(archivo_csv)
  escritor_csv.writerows(temperatura_fenomenos_csv)

# Guardar el diccionario en un archivo JSON
with open("temperaturas.json", "w") as archivo_temp:
  json.dump(temperatura_fenomenos_dict, archivo_temp)
