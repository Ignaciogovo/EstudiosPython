#Funciones

# Definicion de una función.


def funcion():
    return ("Hola")

def funcionvariables(variable1,variable2):
    print("Hola %s, tienes %s" %(variable1,variable2))

def funcionvariables2(variable1=None,variable2=None): # El valor predeterminado.
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

# Uso de args y kwargs en python
# *args --> Numero de argumentos variable
def suma(*args):
    s=0
    for arg in args:
        s+=arg
    return(s)
print(suma(23,3,4,5,6,6))

# **kwargs:
def suma(**kwargs):
    s=0
    for key,value in kwargs.items():
        print(key, "=", value)
        s+=value
    return(s)
print(suma(a=3, b=10, c=3))





# Realización de un menú en python de los procedimientos:


import inspect  # --> Con este modulo puedes ver los argumentos que necesita una un procedimiento.
procedimientos=[funcion,funcionvariables,funcionvariables2]
for i, procedimiento in enumerate(procedimientos):
    print(str(i+1)+": "+procedimiento.__name__)         ##### __name___ es para saber el nombre del procedimiento guardado en la varriable
    firma=inspect.signature(procedimiento)
    parametros=firma.parameters
    print(parametros)
    if len(parametros)==0:
        # Ejecutamos el procedimiento
        procedimiento
    else:
        argumentos=[]
        for parametro in parametros.values():
            print(parametro)
            argumento=input("Ingresa el valor del parametro: "+str(parametro))
            argumentos.append()
        procedimiento(*argumentos)
