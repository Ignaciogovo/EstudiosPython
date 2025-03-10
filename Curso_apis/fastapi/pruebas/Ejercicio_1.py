# uvicorn main:app --reload
# ✔ main → Nombre del archivo (main.py).
# ✔ app → Nombre de la instancia de FastAPI (app = FastAPI()).
# ✔ --reload → Habilita recarga automática (ideal para desarrollo).




# Ejercicio 1
# vamos a desarrollar una API en FastAPI para gestionar productos. 
# Implementaremos operaciones CRUD utilizando métodos HTTP (GET, POST, PUT, DELETE) y validaremos los datos con Pydantic.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
app = FastAPI()

# Definir las categorías permitidas
class TipoProducto(str, Enum):
    alimentacion = "alimentación"
    limpieza = "limpieza"
    belleza = "belleza"
    alcohol = "alcohol"
#Un producto
class Producto(BaseModel):
    id: Optional[int] = None # Opcional para el post ya que se genera automáticamente
    nombre: str = Field(min_length=2,max_length=100)
    tipo: TipoProducto
    precio: float = Field(gt=0,description="El precio debe ser mayor que 0")
    peso: float = Field(gt=0,description="El el peso debe ser mayor que 0")
    stock: int = Field(ge=0,description="El stock no puede ser negativo")


# productos iniciales
productos = [
    {"id":1, "nombre":"Bolsa de patatas","tipo":"alimentación","precio":5,"peso":2,"stock":1000},
    {"id":2,"nombre":"Kit limpieza","tipo":"limpieza","precio":3,"peso":1.2,"stock":1000},
    {"id":3,"nombre":"perfume","tipo":"belleza","precio":15,"peso":0.3,"stock":1000},
    {"id":4,"nombre":"perfume bustamante","tipo":"belleza","precio":150,"peso":0.1,"stock":1000},
    {"id":5,"nombre":"Cerveza","tipo":"alcohol","precio":1.5,"peso":0.5,"stock":500},
    {"id":6,"nombre":"Vodka","tipo":"alcohol","precio":7,"peso":1,"stock":500}

]

def menor_edad(edad: int) -> bool:
    return edad < 18

def ocultar_mayores_edad(productos_final: list,edad):
    if menor_edad(edad):
        return [producto for producto in productos_final if producto["tipo"] != "alcohol"]
    return(productos_final)        



# GET: ruta principal
@app.get("/")
def obtener_mensaje():
    return {"mensaje": "Bienvenido a los productos del supermercado"}

# GET: Obtener todos los productos
@app.get("/productos")
def obtener_productos(edad: int = 17):
    return(ocultar_mayores_edad(productos,edad))



# GET: Obtener un producto
@app.get("/productos/{id}", response_model=Producto)
def obtener_producto(id: int, edad: int = 17):
    productos_finales = ocultar_mayores_edad(productos,edad)
    producto = next((p for p in productos_finales if p["id"] == id), None) # next: Si no encuentra ningún id es None
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


#http://127.0.0.1:8000/docs (Para probar a insertar nuevos productos)
#POST: Agregar un nuevo producto 
@app.post("/productos",response_model=Producto)
def agregar_producto(producto:Producto):
    nuevo_id = max([p["id"] for p in productos] +[0]) +1 # Se genera un nuevo id, si no hubiera productos, el valor sería 0 (De ahí la suma de [0]) 
    nuevo_producto = producto.dict()
    nuevo_producto["id"] =nuevo_id
    productos.append(nuevo_producto)
    return(nuevo_producto) 




#DELETE
@app.delete("/producto/{id}", response_model=Producto)
def eliminar_producto( id: int):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    productos.remove(producto)

    return(producto)



#Actualizar
@app.put("/productos/{id}", response_model=Producto)
def actualizar_producto(id: int, producto_actualizado: Producto):
    for index, producto in enumerate(productos):
        if producto["id"] == id:
            productos[index] = producto_actualizado.dict()
            productos[index]["id"] = id  # Mantener el mismo ID
            return(productos[index])
    raise HTTPException(status_code=404, detail="Producto no encontrado")
    