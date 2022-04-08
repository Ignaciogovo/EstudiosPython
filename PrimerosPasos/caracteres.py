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
mensaje1 = mensaje.find("mundo") #Devuelve la posicion en la que empieza la subcadena.
    #Si no lo encuentra el valor es: -1

mensaje2 = mensaje.count("a") #Devuelve la posicion de la subcadena
mensaje2 = mensaje.count("a",1,5) # Empieza a buscar desde la primera posicion hasta la quinta.

#Validación:
mensaje3 = mensaje.startswith("h") # Devuelve true si la cadena empieza por h
mensaje3 = mensaje.endswith("h") # Devuelve true si la cadena termina por h
mensaje3 = mensaje.islower() # Devuelve true si esta en minuscula
mensaje3 = mensaje.isupper() # Devuelve true si esta en mayuscula

#Minúsculas y mayúsculas:
minusculas = mensaje.lower()
mayusculas = mensaje.upper()
PrimeraMayuscula =  mensaje.capitalize() # Devuelve la primera en mayuscula
Invertido = mensaje.swapcase() # Devuelve las minusculas en mayusculas y viceversa
Titulos = mensaje.title() # Devuelve las letras despues de un espacio en mayuscula


#Remplazar
mensaje1 = mensaje.replace("l", "pizza")
mensaje1 = mensaje.strip() #Devuelve la cadena sin los espacios del principio ni final
mensaje1 = mensaje.strip("h") #Devuelve la cadena sin las letras mencionadas del principio ni final

#Cortar
mensajeacortado = mensaje[1:8] # --> ola Mun 
mensajeacortado = mensaje[:8] # -->  Hola Mun       Coge desde el principio



#Convertir una cadena en una lista:
hora = "12:23:12"
print(hora.split(":"))
#Devuelve:['12', '23', '12']


#Poner comillas, espacios y saltos de linea en una cadena de texto
    # \" --> Comillas
    # \t --> Espacios
    # \n --> Saltos de linea
print('\"Hola\tMundo\nViva\ter\tBetis\"') # -->  "Hola   Mundo
                                            #Viva    er      Betis"
#Para no tener problemas con \:
print(r'\Hola\tMundo\nViva\ter\tBetis\ ') # --> \Hola\tMundo\nViva\ter\tBetis\