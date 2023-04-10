from fastapi import APIRouter, HTTPException
from pydantic import BaseModel # --> método de validación
#Pydantic hace que sea fácil definir modelos de datos precisos y validar los datos de entrada. Con Pydantic, podemos estar seguros de que los datos que recibimos se ajustan al modelo definido y evitar errores.
                    ### prefix prefijo de la api, tags= nombre para diferenciar distintas apis, responses, respuesta generica en caso de error
router = APIRouter(prefix="/products", tags=["Products"], responses={404:{"message":"No encontrado"} })
products= ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5", "Producto 5"]

@router.get("/")
async def select_products():
    return products

@router.get("/{id}")
async def select_products(id:int):
    if id in products.index():
        return products[id]
    else:
        return "No se encuentra el producto"