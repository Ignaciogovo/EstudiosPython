# Los modulos son archivos .py que implementa un conjunto de funciones a partir de otros archivos .py
import Funciones #Importamos un archivo de nuestra carpeta
# Usamos una funcion de ese archivo.
print(Funciones.funcion())

#Hay muchos modulos incorporados:
# funciones con los import
# Ejemplo: urllib --> Permite crear datos de lectura a partir de URLs
import urllib
print(dir(urllib)) # --> muestra los paquetes de ese modulo
print(help(urllib.__path__))
# Escribir parquetes