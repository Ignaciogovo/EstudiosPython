from fastapi import FastAPI
from pydantic import BaseModel # --> método de validación
#Pydantic hace que sea fácil definir modelos de datos precisos y validar los datos de entrada. Con Pydantic, podemos estar seguros de que los datos que recibimos se ajustan al modelo definido y evitar errores.

app = FastAPI()

# uvicorn users:app --reload

@app.get("/usersjson")
async def read_usersjson():
    return [{"name": "Nombre","surname":"Apellido","url":"prueba.com"},
    {"name": "Nombre2","surname":"Apellido2","url":"prueba2.com"},
    {"name": "Nombre3","surname":"Apellido3","url":"prueba3.com"}]



# POO
# entidad user:
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int




users_list=[User(id= 1,name="Nombre",surname="Apellido",url="prueba.com",age=24),User(id= 2,name="Nombre2",surname="Apellido2",url="prueba2.com",age=34),User(id= 3,name="Nombre3",surname="Apellido3",url="prueba3.com",age=27)]

@app.get("/users")
async def users():
    return users_list



# Generamos una función de busqueda de usuario
def search_user(id):
    users= list(filter(lambda user: user.id==id, users_list))
    try:
        return users[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    

# Escoger un usuario entre varios
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)



# Otra opción: userquery:
# url= http://127.0.0.1:8000/userquery?id=1
@app.get("/userquery")
async def user(id:int):
    return search_user(id)








#### post
## Añadimos un usuario
@app.post("/user")
async def insert_user(user: User):
# Comprobamos si el id del usuario existe
    if type(search_user(user.id)) == User:
        return "El usuario ya existe"
    else:
        users_list.append(user)
        return users_list[-1]





####Delete
## Borramos un usuario
@app.delete("/user")
async def insert_user(user: User):
# Comprobamos si el id del usuario existe
    
    if type(search_user(user.id)) == User:
        users_list.remove(search_user(user.id))
        return users_list
    else:
        return "El usuario no existe"
