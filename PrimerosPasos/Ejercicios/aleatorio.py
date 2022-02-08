# Problema 1:
# print("Tirar dos dados imprimir si la suma de los mismos es igual a 7")
# Necesitamos exportar random de la biblioteca estándar de Python
import random
dado1= random.randint(1,6) # Genera un número aleatorio del 1 al 6
dado2= random.randint(1,6)
print("Primer dado es %d" % dado1)
print("Segundo dado es %d " % dado2)
suma = dado1 + dado2
print("La suma es: %d" % suma)
if suma == 7:
    print("Has ganado")
else:
    print("No es igual ha 7 por tanto has perdido")


# Problema 2:
# Generar numeros aleatorios, meterlos en una lista, imprimirlos y mezclarlos.
def cargar():
    lista = []
    for variable in range(10):
        lista.append(random.randint(0,1000))
    return lista
def imprimir(lista):
    print(lista)
def desordenar(lista):
    random.shuffle(lista)

# lista = cargar()
# imprimir(lista)
# desordenar(lista)
# imprimir(lista)

import random
# Problema 2:
# Generar un número entre el 1 al 15 e intentar adivinarlo. 
numero = random.randint(1,10)
while True:
    prueba = int(input("Elige un número del uno al 10: "))
    if prueba == numero:
        print("has acertado")
        break # sale del bucle


