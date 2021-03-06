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
