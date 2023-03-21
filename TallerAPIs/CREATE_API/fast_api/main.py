from fastapi import FastAPI
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

