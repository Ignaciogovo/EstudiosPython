# Esto es un comentario.
"""

Esto es un comentario de varias lineas

"""



# Variables
# Cada variable es un objeto. Así que cada objeto soporta estas instrucciones:
# help(object) --> Muestra la información de cómo usar cada objeto
# dir(object) --> muestra la estructura interna del objeto

# 1 Numeros:
numero = 19
    # floats:
decimal = 7.0
decimal2= float(7)
int(8) # --> Para convertir una cadena de texto en integer

# 2 Cadenas:
nombre_variable = "valor variable"
prueba = "prueba"
# 3 Operadores:
numeros = 1 +2 *3 / 3.0
resto = 11 % 3
    # potencias
cuadrado = 7 ** 2
cubico = 7 ** 3
uno = 1
dos = 2
tres = uno + dos

hola = "hola"
mundo = "mundo"
holamundo = "hola" + " " + mundo


#Se puede asignar más de una variable de forma simultanea: 
a, b = 3, 2

# 4 imprimir por pantalla
print(nombre_variable)
    # Concatenar
print(f"{nombre_variable} - {numero} - {prueba}")
print(nombre_variable + " - " + str(numero) + " - " + prueba) # --> str() Es para convertir una variable en cadena de texto | Para concatenar de esta forma tiene que ser el mismo tipo de dato
    # Operador % para las print
    # Ejemplo:
datos = ("Juan", "Perez", 53.44)
print("Hola %s %s. Tu balance es de %.2f" % (datos[0],datos[1],datos[2]))
    # %s - Cadena (O cualquier objeto, como los números al representarlos en una cadena de texto)
    # %d - Integer
    # %f - Números de punto flotante
    # %.<numero de digitos>f - Números de punto flotante con una cantidad de números fijos a la derecha del punto.
    # %x/%X - Integer con representacion hex (minúscula/mayúscula)

# 5 operaciones con los strings
unacadena = "Hola mundoooo"
print (len(unacadena)) #Cuenta el numero de caractareres que hay en el string ( contando puntuación y espacios)
print (unacadena.count("o")) #Devuelve el número de veces que se usa el caracter o.
print (unacadena.upper()) # devuelve todas las letras en mayuscula.
print (unacadena.lower()) # Devuelve todas las letras en minuscula.
print (unacadena.index("o")) # devuelve la posición de la primera o
lista = unacadena.split(" ") # convierte en valores de una lista todas los caracteres separados por un espacio.
# 6 Entrada de datos
edad = input("Cual es tu edad?: ")
# Valor por defecto:
input = input("Cual es tu edad?: ") or ("23")




# Enlaces
# Pedir un valor hasta que sea verdadero https://www.codigopiton.com/pedir-valor-al-usuario-hasta-que-sea-valido-en-python/













































# #Condiciones
# if int(edad) < 18: #-> int convierte una cadena en un int.
#     print("Eres menor de edad")
# else:
#     print("Eres mayor de edad")

# Funciones

def mostrarEdad(edad):
    resultado = ""
    if int(edad) < 18: #-> int convierte una cadena en un int.
        resultado = "Eres menor de edad"
    else:
        resultado = "Eres mayor de edad"

    return resultado

print(mostrarEdad(edad))



# arrays
variables = ["variable1", "variable2", "variable3"]

# for
for variable in variables:
    print("- " + variable)
