cadena_de_texto = 'nif;nombre;email;telefono;descuento\n01234567L;Luis  Gonzalez; luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena  Ramirez; macarena@mail.com;692839321;8\n63823376M;Juan  Jose  Martinez; juanjo@mail.com;664888233;5.2\n98376547F;Carmen  Sanchez; carmen@mail.com;667677855;15.7'

salida = {}

lista_datos = cadena_de_texto.split('\n')
titulos = lista_datos.pop(0)

for datos in lista_datos:
    datos_clientes = datos.split(';')
    salida[datos_clientes[0]]=dict(zip(titulos.split(';')[1:],datos_clientes[1:]))

print(salida)