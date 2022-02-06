#Las tuplas son como las listas pero no se pueden modificar. No se puede añadir, eliminar, mover, etc..
#Ventajas: Son más rapidas, menos espacio, Pueden utilizarse como clave en un diccionario(Las listas no)


tupla = (1,2,3,"variable2",4,5)
print (tupla)


# Convertir tuplas en listas
lista = list(tupla)
print(lista)

# Convertir listas en tuplas
tupla = tuple(lista)


#Desempaquetado de tuplas
mitupla = ("Juan,",13,1,1996)
nombre,dia,mes,year = mitupla
print(nombre)
print(dia)