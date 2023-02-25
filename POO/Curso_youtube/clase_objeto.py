# Clase: coche, auto ropa



# Definir una clase: (Aconsejable primera letra en mayuscula)
class Auto:
    marca = ""
    year = 0
    matricula = ""


# Definir un objeto:
taxi= Auto()

# Imprimir un atributos por pantalla
print(taxi.year)




# Incluir atributos fuera de la clase

class Nombre:
    pass

# Creamos un objeto
nombre1=Nombre()
nombre2 = Nombre()
# Incluimos atributos
nombre1.edad = 23
nombre2.edad = 12
# Imprimos atributos
print(nombre2.edad)


# Metodos:
class Persona:
    edad = 0
    genero = ""
    nombre = ""
    # Incluimos un metodo en la clase
    def mayoria(self):
        if self.edad >=18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
persona1 = Persona()
persona1.edad = 23
persona1.mayoria()


############### Metodos especiales ###############33

# Metodo __init__

class Ropa:
    def __init__(self):
        self.marca = 'Willow'
        self.talla= 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.marca)


# Ejemplo calculadora:
class Calculadora:
    def __init__(self,n1,n2) -> None:
        self.suma = n1+n2
        self.resta = n1-n2 
        self.multipicacion=n1*n2 
        self.division=n1/n2

operacion = Calculadora(7,2)
print(operacion.multipicacion)




## Funciones para atributos:
# getattr
class Persona:
    edad = 0
    genero = ""
    nombre = ""

doctor = Persona()

print("La edad es:", doctor.edad)
print("La edad es:", getattr(doctor,'edad'))


# hasattr # Devuelve true si tiene ese atributo
print("¿Tiene una edad?", hasattr(doctor,'edad'))  # Devuelve true si esta ese atributo en el objeto



# setattr # modificar el valor de un atributo
setattr(doctor,'nombre','Paco')



# Borrar valor de atributo:
delattr(doctor,'nombre')



# Constructor
class Persona:
    def __init__(self,nombre,año) -> None:
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return ' {} tiene {}'.format(self.nombre,self.año) # El format es una forma para imprimir un varchar con variables
    
    def comentario(self,frase):
        return '{} dice {}'.format(self.nombre, frase)

paco = Persona("paco",23)
print(paco.comentario("Pariatur ipsum sint Lorem commodo labore nulla sit."))
print(paco.descripcion())



# Ejemplo constructor:
class Email:
    def __init__(self) -> None:
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
# Comprobamos que el correo no se ha enviado
print(mi_correo.enviado)
# Ejecutamos la función enviar_correo
mi_correo.enviar_correo()
# Comprobamos que el atributo ha cambiado
print(mi_correo.enviado)






###################### Herencia
## Es crear una nueva clase a partir de las existentes
# Clase padre
class Pokemon:
    pass
    def __init__(self,nombre,tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es de tipo: {}'.format(self.nombre,self.tipo)
# Clase hijo
class Pikachu(Pokemon):
    def ataque(self,tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)


class Charmander(Pokemon):

    def ataque(self,tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)



# Cogemos la clase hijo 
nuevo_pokemon = Pikachu("Pikachu","Electrico")
# Función de la clase hijo
print(nuevo_pokemon.ataque("relampago"))
# Aqui usamos una función de la clase padre
print(nuevo_pokemon.descripcion())




# Ejercicio practico calculadora
class Calculadora:
    def __init__(self,numero) -> None:
        self.n= numero
        self.datos = [0 for i in range(numero)]
    def ingresardato(self):
        self.datos = [int(input('Ingresar datos '+str(i+1)+ '= ')) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self, numero) -> None:
        Calculadora.__init__(self,2)
    def suma(self):
        a,b = self.datos
        s = a+b
        print("El resultado es :",str(s))
    def resta(self):
        a,b = self.datos
        s = a-b
        print("El resultado es :",str(s))


class Raiz(Calculadora):
    def __init__(self, numero) -> None:
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es: ', math.sqrt(a))
calculo = Raiz(4)
calculo.ingresardato()
calculo.cuadrada()