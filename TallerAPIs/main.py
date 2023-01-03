import requests
import json
if __name__ == '__main__': # Especifica si el archivo principal(Es decir, si este archivo es modulo de otro archivo no se ejecutaria cuando se ejecuta el segundo archivo)
    url = 'http://httpbin.org/post' # Tambien se puede con get, se ven menos atributos
    args = { 'nombre': 'Betis', 'curso': 'python', 'nivel': 'intermedio'} # Es igual que poner en la url esto: http://httpbin.org/get?nombre=Betis&curso=python
    payload = { 'nombre': 'Betis', 'curso': 'python', 'nivel': 'intermedio'}
    # response= requests.post((url), params=args) # Tambien se puede con get, se ven menos atributos
    response= requests.post((url), data=json.dumps(payload)) # Tambien se puede con get, se ven menos atributos
    # json


    print(response)
    print(response.url) # Extraer la url
    # print(response)
    if response.status_code == 200:
        content=response.content
        print(content)


    # extraer un json
    if response.status_code==200:
        response_json=response.json() # Devuelve un diccionario
        print(response_json)
        origin = response_json['origin']
        print(origin)

    # con libreria json
    if response.status_code ==200:
        response_json=json.loads(response.text)
        




# estatus code: 
# Clases de estado de respuesta HTTP

# Estas pueden ser de 5 tipos según sea su necesidad:

#     Respuestas informativas (100-199), que establecen cómo va el programa de código.
#     Respuestas satisfactorias (200 – 299), que se encargan de mostrarte lo que está funcionando correctamente con el programa.
#     Redirecciones (300 – 399), que permiten saber de qué manera se están relocalizando los enlaces de navegación de las peticiones.
#     Errores de los clientes (400 – 499), que te permiten saber de qué forma ha errado el usuario en la ejecución del programa de código.
#     Errores de los servidores (500 – 599), cuya causa son problemas originarios del servidor y no de alguna acción que tú o el usuario hayáis efectuado. Estos pueden solucionarse cuando el servidor esté funcionando correctamente otra vez. 