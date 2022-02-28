#crear una variable con una cadena de caracteres
mensaje = "Hola Mundo"

#Concatenar:
mensaje = 'Hola' + '' + 'Mundo'

#Multiplicar:
mensaje = 'Hola Mundo' * 3

#Añadir de manera sucesiva:
mensaje = 'Hola'
mensaje += ' '
mensaje += 'Mundo'

#Indicar el número de caracteres de una cadena: (Los espacios en blanco tambien cuentan)
tamaño = len(mensaje)

# Encontrar:
mensaje1 = mensaje.find("Mundo") #Devuelve la posicion en la que empieza la subcadena.
    #Si no lo encuentra el valor es: -1

#Minúsculas y mayúsculas:
minusculas = mensaje.lower()
mayusculas = mensaje.upper()

#Remplazar
mensaje1 = mensaje.replace("l", "pizza")

#Cortar
mensajeacortado = mensaje[1:8] # --> ola Mun 
mensajeacortado = mensaje[:8] # -->  Hola Mun       Coge desde el principio

#Poner comillas, espacios y saltos de linea en una cadena de texto
    # \" --> Comillas
    # \t --> Espacios
    # \n --> Saltos de linea
print('\"Hola\tMundo\nViva\ter\tBetis\"')