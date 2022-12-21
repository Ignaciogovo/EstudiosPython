### Regular expresions ###
import re
import sys
# in the sys.path list
sys.path.append('/home/ignaciogovo/proyectos/EstudiosPython/prueba')   
import emailEjemplos as emails
my_string = "Esta es la Lección sobre las Expresiones ección lección regulares es la lección número : 7"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# Indica si al principio de la variable encontramos esa linea de texto
print(re.match("Esta es la lección", my_string))
print(re.match("esta es la lección", my_string, re.I)) #Ignora las mayusculas o las minusculas  -------> re.X --> Ignora los espacios en blanco y los comentarios
print(re.match("Esta es la lección", my_other_string)) # Indica si al principio de la variable encontramos esa linea de texto





# match  Indica si al principio de la variable encontramos esa linea de texto
#   #convierte la variable en un objeto:
match = re.match("Esta es la lección", my_string)
if not(match == None):
# if match != None): ---> Otra forma de hacerlo
# if match is not None: ---> Otra forma
    print(match)

    start, end = match.span() # Es una tupla con dos valores
    print(my_string[start:end])


# search --> Busca en toda la cadena
search = re.search("sobre", my_string, re.I)
print(search)
start,end = search.span()
print(my_string[start:end])


# findall incluye la subcadena en un array la cantidad de veces que se encuentra en una variable

findall = re.findall("lección", my_string, re.I)
print(findall)


# split --> Crea una lista divida por el patrón que se indique, en este caso la
print(re.split("la", my_string))

# sub --> Subtituir  origen, final, variable
print(re.sub("lección", "LECCIÓN", my_string))
print(re.sub("lección|Lección", "LECCIÓN", my_string)) # --> Distintas opciones
print(re.sub("[l|L]ección", "LECCIÓN", my_string)) # --> Distintas opciones

# patterns

pattern = r'[lL]ección|Expresiones'
patterns = {
    r'[a-z]' # No incluye tildes
    , r'[A-Z]'
    ,r'[09]'
    ,r'[a-d5-8]' # equivale a [abcd5678]
#    ,r'[-a4]' # para tener un guión como parametro y no como separador
    ,r'[\w]' # (POSIX [[:word:]]): letras minúsculas, mayúsculas, números y guión bajo (_)
    ,r'[.]' # Cualquier caracter
    # ,r'['
    ,r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # hecho para email
    ,r'^hola$' # --> ^ Indica el comienzo y $ Indica el final
    ,r'ab*' #0 o más repeticiones tantas repeticiones como sean posibles. ab* coincidirá con “a”, “ab” o “a” seguido de cualquier número de “b”.
    ,r'ab+' #1 o más repeticiones. ab+ coincidirá con “a” seguido de cualquier número distinto de cero de “b”; no coincidirá solo con “a”.
    ,r'ab?' #0 o 1 repeticiones de la RE precedente. ab? coincidirá con “a” o “ab”.
    ,r'ho{1}la' # Indica el número exacto de repeticiones que tiene la letra o
    ,r'ho{2,6}la' # Número de repeticiones en un rango
    ,r'[^(hola)]' # Excluye el grupo 
}
print("A")
print(re.findall(pattern,my_string))
pattern = r'\d' # No cuenta con los valores no númericos
print("A")
print(re.findall(pattern,my_string))
pattern = r'\D' # No cuenta con los valores númericos
print("A")
print(re.findall(pattern,my_string))

# Ejercicio, comprobar si el email es correcto
print(emails.data)
def comprobar_emails(data):
    list_verificados = []
    for email in data:
        pattern= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.search(pattern,email["email"]):
            list_verificados.append(email["email"])
    
    print("Verificados como email")
    print(len(list_verificados))
    # return('')
    for i in range(0,len(list_verificados)):
        print(str(i)+" "+list_verificados[i])

comprobar_emails(emails.data)


# prueba = ' hola me llamo prueba y esto no es un ejercicio dificil'
# print(re.findall())