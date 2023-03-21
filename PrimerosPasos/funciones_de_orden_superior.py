############ filter: ##################3333

######## Separar los números impares:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_impar(numero):
    return numero % 2 != 0

numeros_impares = list(filter(es_impar, numeros))

print(numeros_impares)


#### Filtrado de palabras por cierta letra:
palabras = ["hola", "adiós", "python", "programación"]

def contiene_letra(palabra, letra):
    return letra in palabra

palabras_con_t = list(filter(lambda x: contiene_letra(x, "t"), palabras))

print(palabras_con_t)


# filtrado mayor que
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def mayor_que(numero, valor):
    return numero > valor

numeros_mayores_a_50 = list(filter(lambda x: mayor_que(x, 50), numeros))

print(numeros_mayores_a_50)





# lambda:
# Lambda es una función anónima en Python que se utiliza para crear pequeñas funciones que se pueden utilizar en el momento sin necesidad de definirlas previamente. La sintaxis general de una función lambda es la siguiente:


# Conceptos
# lambda argumentos : expresión



#Ejemplo sin lambda:
def cuadrado(numero):
    return numero**2

resultado = cuadrado(5)
print(resultado)  # resultado = 25

#Ejemplo con lambda:
cuadrado = lambda numero: numero**2

resultado = cuadrado(5)
print(resultado)  # resultado = 25