from fastapi import APIRouter, HTTPException
from pydantic import BaseModel # --> método de validación
#Pydantic hace que sea fácil definir modelos de datos precisos y validar los datos de entrada. Con Pydantic, podemos estar seguros de que los datos que recibimos se ajustan al modelo definido y evitar errores.

router = APIRouter(prefix="/user", tags=["Users"], responses={404:{"message":"No encontrado"} })

# uvicorn users:app --reload

@router.get("/usersjson")
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

@router.get("/")
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
@router.get("/{id}")
async def user(id:int):
    return search_user(id)



# Otra opción: userquery:
# url= http://127.0.0.1:8000/userquery?id=1
@router.get("/userquery")
async def user(id:int):
    return search_user(id)








#### post
## Añadimos un usuario
########### Aquí usamos el formato de error HTTPException y como devolverlo
@router.post("/", status_code=201)
async def insert_user(user: User):
# Comprobamos si el id del usuario existe
    if type(search_user(user.id)) == User:
        # Realizar una excepción
        raise HTTPException(status_code=404,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return users_list[-1]




#### put
## Actualizamos el usuario
@router.put("/")
async def update_user(user: User):
    if type(search_user(user.id)) == User:
        users_list[users_list.index(search_user(user.id))]=user
        return users_list
    else:
        return {"error": "El usuario no existe"}

####Delete
## Borramos un usuario
@router.delete("/")
async def delete_user(user: User):
# Comprobamos si el id del usuario existe
    
    if type(search_user(user.id)) == User:
        users_list.remove(search_user(user.id))
        return users_list
    else:
        return {"error": "El usuario no existe"}



## ESTADOS HTTP
# Aciertos
# 200 --> get
# 201 --> post /insert


# errores