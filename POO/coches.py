#Crear una clase:
class coche():
    # ---> Estas son las propiedades
    largoChasis=250             
    anchoChasis=120
    ruedas=4
    enmarcha=False
    # ---> Estos son los comportamientos.
    def arrancar(self): # self hace referencia al objeto de la clase
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche esta parado"

# Crear objeto
micoche=coche()  # instanciamos una clase.
print("El largo del coche es: ",micoche.largoChasis) #mostrar cararcteristicas del coche.

# Cambiar el comportamiento del objeto:
micoche.arrancar()
print(micoche.estado())