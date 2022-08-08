try:
    a = int("prueba")
except:
    print("prueba finalizada pero seguimos con el script")

# CREAR UNA CLASE:
class auto:
    pass

# Crear atributos predeterminados a una clase y funciones
class auto:
    rojo = False
    def __init__(self): # init: Se crea el objeto, se inicializa de forma automatica al crear el objeto. self es la propia variable
        print("se creó el auto")
    def fabricar(self):
        self.rojo = True
# Crear un objeto:
# taller = auto()

# # Añadir atributo a un objeto:
# taller.color = "rojo"
# taller.puertas = "De 1 a 8"



# clase más completa:
class auto:
    rojo= False
    # Indicar parametros iniciales a parte de self
    def __init__(self,puertas=None,color=None):
        self.puertas = puertas
        self.color = color
        if puertas is not None and color is not None:
            print("Se ha creado un auto con puertas %s y color %s" %(self.puertas,self.color))

# a = auto("4","Blue")



# Metodos especiales

class fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto", self.nombre)
    
    def __del__(self): # Elimina el objeto creado anteriormente si se genera otro nuevo o lo elimina al final del script
        print("Se elimino el auto", self.nombre)

    def __str__(self): # string que forma parte del objeto
        return "{}  se fabricó con exito, en el tiempo {} y tiene esta cantidad de ruedas {}".format(self.nombre,self.tiempo,self.ruedas)

    def __len__(self): # Indica la duración o longitud del objeto:
        return self.tiempo
a = fabrica(10,"auto",4)
a = fabrica(10,"rico",4)


# Para ejecutar la funcion __str__
print(a)

# Para ejecutar la funcion __len__
len(a)