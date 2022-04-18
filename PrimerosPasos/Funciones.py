#Funciones

# Definicion de una función.

from asyncio.windows_events import NULL


def funcion():
    return ("Hola")

def funcionvariables(variable1,variable2):
    print("Hola %s, tienes %s" %(variable1,variable2))

def funcionvariables2(variable1=NULL,variable2=NULL): # El valor predeterminado.
    print("Hola %s, tienes %s" %(variable1,variable2))


# convertir argumentos en listas:
def funcionArgumentos(*argumentos):
    for argumento in argumentos:
        print(argumento)
#funcionArgumentos("prueba",1,2,3,4,"Prueba2")

# Convertir argumentos en diccionarios:
def funciondiccionarios(**argumentos):
    print(argumentos)
    print(" ")
    for clave in argumentos:
        print(clave, " ",argumentos[clave])

#funciondiccionarios(nombre="Prueba",apellidos="prueba1 prueba2",notas=[1,2,4])


#Funciones recursivas:
def cuentatras(segundos):
    segundos-=1
    if segundos >= 0:
        print(segundos)
        cuentatras(segundos)
cuentatras(9)
#llamada de funcion
# print (funcion())
    

