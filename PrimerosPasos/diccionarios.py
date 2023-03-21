# Un diccionario es similar a los arreglos pero trabaja con llaves y valores.
# Por ejemplo una base de datos de telefonos:

librotelefonico1 = {}
librotelefonico1["Juan"] = 938477566
librotelefonico1["Jack"] = 938377264
librotelefonico1["Jill"] = 947662781


# Otra forma:
librotelefonico = {
    "Juan" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# Iterar un diccionario:
# for name, number in librotelefonico.iteritems():
#     print("numero telefonico de %s es: $d" %(name,number))

# añadir
librotelefonico1["mike"] = 000000000
# modificar
librotelefonico1["mike"] = 986652781
# Combinar diccionarios:
librotelefonico1.update(librotelefonico)
# Borrar 
del librotelefonico1["Jill"]
print(librotelefonico1)


# Usar una tupla para asigarnar las keys de un diccionario
naciones = ["España","Francia", "Alemania"]
capitales = {naciones[0]:"Madrid", naciones[1]:"Paris",naciones[2]:"Berlín"}
print(capitales)

# Imprimir valores 
print(capitales.values())
# Imprimir keys
print(capitales.keys())

# Comprobar si una clave se encuentra en el diccionario:
if "España" in capitales:
    print (capitales["España"])


# Recorrer un diccionario junto su valor:
for x in capitales:
    valor = capitales.get(x)
    print(x," --> ",valor)



# Copiar un diccionario
# Hay que tener en cuenta que de la forma normal el diccionario se queda vinculado al original
x = capitales
# Si cambias algo del diccionario x, cambiara del de capitales y viceversa

# Para desvincular la mejor occión es:

x = capitales.copy()

# Otra opción es:
x = dict(capitales)


# Combinar 2 Diccionarios
persona1 = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
persona2 = {'nombre': 'María', 'edad': 25, 'ciudad': 'Barcelona'}
personas = list(zip(persona1.items(), persona2.items()))

print(personas)
# Resultado: [(('nombre', 'Juan'), ('nombre', 'María')), (('edad', 30), ('edad', 25)), (('ciudad', 'Madrid'), ('ciudad', 'Barcelona'))]
