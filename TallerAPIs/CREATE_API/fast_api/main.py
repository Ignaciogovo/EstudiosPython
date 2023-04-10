from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import  StaticFiles
from routers.users import User,search_user,users_list
from routers import products, users

app = FastAPI()

# Ejecutar servidor local: uvicorn main:app --reload


## Obtener a la documentación:
# http://127.0.0.1:8000/docs

## Documentación alternativa
# http://127.0.0.1:8000/redoc



# Creamos una función
@app.get("/")
async def root():
    return "Hola mundo"

# Realizar otra función a partir de una url
@app.get("/url")
async def url():
    return{"url_curso":"prueba/.com"}
# http://127.0.0.1:8000/url




## TIPOS DE ACCIONES:
# post: crear datos
# get: leer datos
# put: actualizar datos
# delete: borrar datos
# Para ver ejemplos: users.py

###Uso de estados de HTTP


#### Modificación del código de estado para acierto
@app.post("/user", status_code=201)
async def insert_user(user: User):
# Comprobamos si el id del usuario existe
    if type(search_user(user.id)) == User:
########## Modificación del código del estado en caso de error        # Realizar una excepción
        raise HTTPException(status_code=404,detail="El usuario ya existe")
    else:
        users_list.append(user)
        return users_list[-1]



### ROUTERS
### importar routers
app.include_router(products.router)
app.include_router(users.router)

### recursos estaticos    (imagenes)
app.mount("/static",StaticFiles(directory="static"),name ="static")