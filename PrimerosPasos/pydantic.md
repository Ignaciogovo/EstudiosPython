# *Pydantic*





## ¿Qué es?
-- Ayuda a validar y estructurar datos de manera fácil y segura


## Ejemplo
```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# Definir las categorías permitidas con Enum
class TipoProducto(str, Enum):
    alimentacion = "alimentación"
    limpieza = "limpieza"
    belleza = "belleza"
    alcohol = "alcohol"

# Definir el modelo de datos con Pydantic
class Producto(BaseModel):
    id: Optional[int] = None  # Puede ser opcional (para cuando se crea un nuevo producto)
    nombre: str = Field(min_length=2, max_length=100)  # Nombre con mínimo 2 caracteres y máximo 100
    tipo: TipoProducto  # Solo puede ser uno de los valores definidos en TipoProducto
    precio: float = Field(gt=0, description="El precio debe ser mayor que 0")  # Precio debe ser mayor que 0
    peso: float = Field(gt=0, description="El peso debe ser mayor que 0")  # Peso mayor que 0
    stock: int = Field(ge=0, description="El stock no puede ser negativo")  # Stock mayor o igual a 0


```

## Field
-- Genera reglas con valores mínimos, máximos y descripciones
Casos:
| Opción | ¿Qué hace?  | Ejemplo |
|:------------- |:---------------:| -------------:|
| min_length=2  | min caracteres  | nombre: str = Field(min_length=2)        |
| max_length=2  | max caracteres  | nombre: str = Field(max_length=100)      |
| gt=0       | > 0      | precio: float = Field(gt=0)        |
| ge=0        | >= 0 | stock: int = Field(ge=0)        |
| lt=1000 |	< 0 |	stock: int = Field(lt=1000) |
| le=0  | <= 0 | stock: int = Field(ge=0)        |
| regex="^[A-Za-z]+$"  | Validar formato con expresiones regulares | nombre: str = Field(regex="^[A-Za-z]+$")     |
| description="Texto"  | Agregar descripción | precio: float = Field(gt=0, description="Debe ser positivo")     |


## @validator
-- Permite definir validaciones personalizadas (Más avanzado que field)
✅ Verificar formatos específicos (emails, contraseñas, etc.).
✅ Evitar valores inválidos (números negativos, fechas incorrectas).
✅ Aplicar transformaciones antes de almacenar los datos.

### Ejemplos:
 Email:

 ```python
class Usuario(BaseModel):
    email: str

    @validator("email")  # Se ejecuta cuando se valida el campo "email"
    def validar_email(cls, value):
        if "@" not in value:
            raise ValueError("El email debe contener @")
        return value  # Si es válido, se devuelve el mismo valor

 ```

 
 Validar un teléfono con expresión regular:

  ```python

class Cliente(BaseModel):
    telefono: str

    @validator("telefono")
    def validar_telefono(cls, value):
        if not re.match(r"^\+?[0-9]{7,15}$", value):  
            raise ValueError("El teléfono debe contener entre 7 y 15 dígitos")
        return value
 ```