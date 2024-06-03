# Librerías
import pandas as pd
from time import localtime

# Funciones
def filtrar_por_presupuesto(muebles_df, presupuesto):
    '''
    Filtra los datos del data frame según un presupuesto dado, al verificar si son menores o iguales al
    presupuesto dado.
    '''
    return muebles_df[muebles_df.precio <= presupuesto]

# Declaración de variables
año_actual = localtime().tm_year

# Leer la base de datos
muebles_df = pd.read_json('muebles_bd.json')

# Filtrar por zona
zona_A_df = muebles_df[muebles_df.zona == 'A']
zona_B_df = muebles_df[muebles_df.zona == 'B']

# Calculo del precio de cada inmueble según su zona
precio_A_df = (zona_A_df.metros * 1000 + zona_A_df.habitaciones * 5000 + zona_A_df.garaje * 15000) * ((1 - (zona_A_df.año - año_actual))/100)
precio_B_df = (zona_B_df.metros * 1000 + zona_B_df.habitaciones * 5000 + zona_B_df.garaje * 15000) * ((1 - (zona_B_df.año - año_actual))/100) * 1.5
precio_df = pd.concat([precio_A_df, precio_B_df])

# Agregar la nueva columna al data frame
muebles_df['precio'] = precio_df.sort_index()


print(filtrar_por_presupuesto(muebles_df, presupuesto = 20000))
