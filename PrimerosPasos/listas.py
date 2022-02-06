# 3 Listas
    # Las listas son muy parecidas a los arreglos.
    # Como crear una lista:
lista = [1,2,3]

    # Recorrer lista
for x in lista:
    print(x)

    # De forma individual
print (lista[0])
print (lista[0:3]) # --> Indica los tres primeros elementos

    # Incluir datos en la lista
lista.append("prueba1") # --> añade un valor al final
lista.insert(2,"prueba2") # --> añade un valor en el key asignado.
lista.extend(["valor1",2,"valor3"])
indice = lista.index("Valor1") # --> indica cual es la key del valor pedido. (Con esto indica el primer valor)
print ("prueba2" in lista) # Devuelve true si prueba2 se encuentra en la lista

    # Eliminar elementos
lista.remove("prueba2") # --> Elimina un valor de la lista.
lista.pop() # --> Elimina el ultimo elemento de la lista.


    # Sumar listas

lista1 = ["variable1",2,5,1,"variable3"]
lista2 = ["variable78",2,2,3,"variable8"]
lista3 = lista1 + lista2
