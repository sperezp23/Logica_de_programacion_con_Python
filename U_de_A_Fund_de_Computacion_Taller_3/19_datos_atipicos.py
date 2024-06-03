import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

datos = np.random.standard_normal(1000)
media = datos.mean()
desviacion_std = datos.std()
datos_atipicos_usando_abs = datos[np.abs((datos - media) / desviacion_std) > 3.00]
datos_atipicos = datos[(((datos - media) / desviacion_std) > 3.00) | (((datos - media) / desviacion_std) < -3.00)]

print(f'Datos atípicos (usando abs): {datos_atipicos_usando_abs}\nDatos atípicos (Sin usar abs): {datos_atipicos}')