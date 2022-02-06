# while
from time import sleep

print ("")
variable = 1
while variable <=10:
    print ("Variable " +str(variable))
    variable=variable+1

print ("")
# for
    # 1ª opcion
for variable in range(1,11):
    print ("variable: " +str(variable))

print ("")
    # 2ª opción con arrays:
variables = ["variable1", "variable2", "variable3"]
    # for
for variable in variables:
    print("- " + variable)

print ("")
    # 3ª opción con arrays
for i, variable in enumerate(variables):
    print(str(i)+ " - " + variable)


# Sentencias break y continue
# Muestra 0,1,2,3,4

count = 0
while True:
    print (count)
    count += 1
    if count >= 5:
        break # sale del bucle

# Muestra solo números impares - 1,3,5,7,9
for x in range(10): # Range crea una lista de x numeros seguidos.
    # Chequéa si x es numero par
    if x % 2 == 0:
        continue # Salta esta iteración.
    print (x)


