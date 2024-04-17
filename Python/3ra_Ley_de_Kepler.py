from math import pi
from astropy.constants import G, M_sun
from astropy import units as u

a = float(input(f'Ingrese el valor del semieje mayor en metros [m]:\n'))
usar_astropy = bool(int(input('¿Correr el programa usando astropy?\n[1]: sí\n[0]: no\n')))

if usar_astropy:
    T = (((4*pi**2)/(M_sun*G))*(a*u.meter)**3)**0.5
    print(f'El periodo orbital para el semieje dado es de: {T.to(u.year)}')

else:
    T = (((4*pi**2)/(M_sun.value*G.value))*(a)**3)**0.5
    print(f'El periodo orbital para el semieje dado es de: {T*3.16888e-8} años.')
