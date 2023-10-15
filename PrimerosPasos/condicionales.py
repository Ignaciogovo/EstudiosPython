# Condicionales de una linea:
import sys

x = 2
print (x == 2) # Imprimira en pantalla TRUE
print (x == 3) # Imprimira en pantalla FALSE
print (x < 3)  # Imprimira en pantalla TRUE

# Condicionales if 
x = 1
if x == 2:
    print ("x igual dos!")
elif x > 2:
    print ("mayor que dos.")
else:
    print ("menor que 2")



# Instrucción pass
edad = int(input("¿Cuántos años tiene? "))
if edad < 120:
    pass # Pasa de la orden
else:
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")

# Operadores relacionales
#  == --> si es igual
#  != --> distinto de
# > y <   --> mayor que y menor que


# Operadores logicos:

# Operador and Se tiene que cumplir los dos valores
# operador or. Se tiene que cumplir uno de los dos valores.
# Operador not. Devuelve el valor opuesto.


#Condicionales try and exept:
# Si hay algún tipo de error en el apartado try se ejecutará execpt:
try:
    print("No da error el comando")
except:
    print("Da error")
    # Si queremos salir del programa
    sys.exit(1)



# isinstance!
x = 5
resultado = isinstance(x, int)
print(resultado)  # Esto imprimirá True, ya que x es un entero (int).

# Definimos una variable
valor = 42

# Comprobamos si la variable es un entero
if isinstance(valor, int):
    print("El valor es un entero.")
else:
    print("El valor no es un entero.")





# IF EN LA MISMA LINEA:
resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(resultado)