# 3 Listas
    # Las listas son muy parecidas a los arreglos.
    # Como crear una lista:
lista = [1,2,3,2,2,2,2]
    # Recorrer lista
for x in lista:
    print(x)

    # De forma individual
print (lista[0])
print (lista[0:3]) # --> Indica los tres primeros elementos

    # Incluir datos en la lista
lista.append("prueba1") # --> añade un valor al final
lista.insert(2,"prueba2") # --> añade un valor en el key asignado.
lista.extend(["valor1",2,"valor3"]) # --> añade una lista al final de otra
indice = lista.index("valor1") # --> indica cual es la key del valor pedido. (Con esto indica el primer valor)
print ("prueba2" in lista) # Devuelve true si prueba2 se encuentra en la lista

    # Eliminar elementos
lista.remove("prueba2") # --> Elimina un valor de la lista.
lista.pop() # --> Elimina el ultimo elemento de la lista.
lista.pop(0) # --> Elimina el primer elemento de la lista.

    # count: --> indica cuantos elementos se encuentran en una lista.
    # Vamos a contar cuantas veces se encuentra el elemento 2 en la lista.
print("Numero de veces: ")
print(lista.count(2))
print(len(lista)) # Indica la cantidad de valores que tiene una lista.


# Comprobar que un valor se encuentra en una lista:
if 3 in [1,2,4,5]: # Devuelve 0 o 1 dependiendo si esta o no
    print("Se encuentra")
if 3 not in [1,2,4,5]: # Devuelve 0 o 1 dependiendo si esta o no
    print("No encuentra")
    # Sumar listas

lista1 = ["variable1",2,5,1,"variable3"]
lista2 = ["variable78",2,2,3,"variable8"]
lista3 = lista1 + lista2

# Convertir valores de un dicciconario en una lista:
diccionario = {
    "Juan" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
lista_dicc=list(diccionario.values())

# Eliminar duplicados:
data = [1,3,2,4,7,3,2,2,1,4]
result = []
for item in data:
    if item not in result:
        result.append(item)
        
result

# Combinar 3 listas
nombres = ['Juan', 'María', 'Pedro']
edades = [30, 25, 40]
ciudades = ['Madrid', 'Barcelona', 'Valencia']
personas = list(zip(nombres, edades, ciudades))

print(personas)
# Resultado: [('Juan', 30, 'Madrid'), ('María', 25, 'Barcelona'), ('Pedro', 40, 'Valencia')]



# Desempaquetar una lista de tuplas:
personas = [('Juan', 30), ('María', 25), ('Pedro', 40)]
nombres, edades = zip(*personas)

print(nombres)
# Resultado: ('Juan', 'María', 'Pedro')

print(edades)
# Resultado: (30, 25, 40)


# Diferencias entre dos listas:
    # total = []
    # for lista in (diferencias, dictioanry2):
    #     for item in lista:
    #         if item not in total and not (item  in dictioanry2 and item  in diferencias):
    #             total.append(item)
    # print(total)




# Metodos de desordenar una lista
import random

my_list = [1, 2, 3, 4, 5]

random.shuffle(my_list)
print(my_list)



# Sacar el indice de una lista
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list)):
    value = my_list[i]