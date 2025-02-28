# Temario: Cómo entender las tecnologías de las APIs, de 0 a experto
## Módulo 1: Introducción a las APIs

- ¿Qué es una API? Definición y ejemplos en la vida real.
- Tipos de APIs: REST, SOAP, GraphQL, WebSockets.
- Protocolos y estándares: HTTP, HTTPS, JSON, XML.
- Códigos de estado HTTP: 200, 400, 404, 500 y su significado.

## Módulo 2: Configuración del Entorno con FastAPI

- Instalación de FastAPI y Uvicorn: Configuración básica con pip install fastapi uvicorn.
- Creando nuestro primer endpoint: Configuración básica con @app.get("/").
- Estructura de un proyecto FastAPI: Archivos principales y buenas prácticas.
- Ejecutando la API: Usando uvicorn main:app --reload.

## Módulo 3: Creación de Rutas y Métodos HTTP

- Métodos HTTP en FastAPI: GET, POST, PUT, DELETE.
- Parámetros en las rutas: @app.get("/items/{item_id}").
- Query Parameters y Request Body: Diferencias y usos.
- Validación de datos con Pydantic: Uso de modelos de datos.

## Módulo 4: Manejo de Datos en FastAPI

- Conectando FastAPI con una Base de Datos: Uso de SQLite, PostgreSQL o MongoDB.
- CRUD en FastAPI: Crear, Leer, Actualizar y Eliminar registros.
- Dependencias en FastAPI: Uso avanzado de Depends().

## Módulo 5: Seguridad y Autenticación

- Autenticación con OAuth2 y JWT.
- Manejo de usuarios y permisos.
- Middleware en FastAPI: Protección de rutas.

## Módulo 6: Documentación y Despliegue

- Documentación automática con Swagger y Redoc.
- Desplegando una API con FastAPI: Opciones en servidores como Heroku o AWS.
- Buenas prácticas para producción: Seguridad, logs y monitoreo.


----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------


# **Módulo 1: Introducción a las APIs**  

## **1. ¿Qué es una API?**  
Una **API (Application Programming Interface)** es un conjunto de reglas que permite que dos sistemas se comuniquen entre sí.  

🔹 **Ejemplo en la vida real:**  
Imagina que estás en un restaurante. El **menú** representa los servicios disponibles (los endpoints de la API). Tú **haces un pedido** (solicitud HTTP) y el **mesero** (la API) lo lleva a la cocina (el servidor). Luego, el mesero trae la comida (la respuesta de la API) a tu mesa.  

📌 **Conceptos clave:**  
✅ Cliente (frontend) → Quien solicita datos.  
✅ Servidor (backend) → Quien procesa y responde.  
✅ API → Intermediario entre cliente y servidor.  

---

## **2. Tipos de APIs**  
Existen varios tipos de APIs, pero los más usados son:  

### **🟢 REST (Representational State Transfer)**  
✔ Basado en HTTP.  
✔ Usa formatos como JSON o XML.  
✔ Stateless (sin estado, cada petición es independiente).  
✔ Usa métodos HTTP como `GET`, `POST`, `PUT`, `DELETE`.  
✔ Ejemplo: FastAPI.  

### **🟢 SOAP (Simple Object Access Protocol)**  
✔ Usa XML como formato de datos.  
✔ Más seguro pero más pesado.  
✔ Se usa en sistemas financieros y bancarios.  

### **🟢 GraphQL**  
✔ Permite pedir solo los datos que necesitas.  
✔ Más eficiente en consultas complejas.  
✔ Usado por Facebook, GitHub, etc.  

### **🟢 WebSockets**  
✔ Comunicación en tiempo real (chat, videojuegos).  
✔ Mantiene la conexión abierta entre cliente y servidor.  

---

## **3. Protocolos y estándares en las APIs**  
Las APIs funcionan sobre ciertos protocolos y estándares:  

🔹 **HTTP/HTTPS:** Protocolo de comunicación web.  
🔹 **JSON (JavaScript Object Notation):** Formato ligero de intercambio de datos.  
🔹 **XML (Extensible Markup Language):** Alternativa a JSON, usada en SOAP.  
🔹 **OAuth2 y JWT:** Métodos de autenticación.  

📌 **Ejemplo de una respuesta JSON de una API:**  
```json
{
  "id": 1,
  "nombre": "Carlos",
  "edad": 25
}
```

---

## **4. Códigos de estado HTTP**  
Cuando interactuamos con una API, esta devuelve un **código de estado** que indica el resultado de la solicitud.  

✅ **Códigos de éxito:**  
- `200 OK` → Petición exitosa.  
- `201 Created` → Se creó un recurso nuevo.  

❌ **Errores del cliente:**  
- `400 Bad Request` → Error en la solicitud.  
- `401 Unauthorized` → No autenticado.  
- `404 Not Found` → Recurso no encontrado.  

⚠ **Errores del servidor:**  
- `500 Internal Server Error` → Fallo en el servidor.  
- `503 Service Unavailable` → Servidor no disponible.  

📌 **Ejemplo en FastAPI:**  
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_root():
    return {"mensaje": "¡Hola, mundo! API funcionando correctamente"}
```
✅ Responde con código `200 OK` y un JSON con un mensaje.  

---

### 🎯 **Conclusión**  
- Las APIs permiten la comunicación entre aplicaciones.  
- REST es el estándar más usado en la web.  
- FastAPI facilita la creación de APIs con Python.  
- Los códigos de estado indican el resultado de una solicitud.  


----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------



# **Módulo 2: Configuración del Entorno con FastAPI**  

## **5. Instalación de FastAPI y Uvicorn**  
Antes de comenzar a programar, debemos instalar **FastAPI** y **Uvicorn**, que es el servidor ASGI que ejecutará nuestra API.  

🔹 **Requisitos previos:**  
Asegúrate de tener **Python 3.8 o superior** instalado. Puedes verificarlo con:  
```bash
python --version
```

🔹 **Instalar FastAPI y Uvicorn:**  
Ejecuta el siguiente comando en la terminal:  
```bash
pip install fastapi uvicorn
```

---

## **6. Creando nuestro primer endpoint**  
Una vez instalado, crearemos un **archivo `main.py`** con nuestro primer **endpoint**.  

📌 **Código básico en FastAPI (`main.py`):**  
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_root():
    return {"mensaje": "¡Hola, mundo! API funcionando correctamente"}
```

✔ **Explicación:**  
- `FastAPI()` crea una instancia de la aplicación.  
- `@app.get("/")` define un **endpoint GET** en la ruta `/`.  
- `return {"mensaje": "¡Hola, mundo!"}` devuelve una **respuesta JSON**.  

---

## **7. Estructura de un Proyecto FastAPI**  
Para proyectos más grandes, es recomendable organizar los archivos de esta manera:  

```
📂 mi_api/
 ├── 📂 app/
 │   ├── main.py          # Punto de entrada principal
 │   ├── models.py        # Modelos de datos (Pydantic, SQLAlchemy)
 │   ├── routes.py        # Definición de rutas
 │   ├── database.py      # Configuración de la base de datos
 │   └── config.py        # Configuraciones generales
 ├── venv/               # Entorno virtual (opcional)
 ├── requirements.txt    # Dependencias del proyecto
 └── README.md           # Documentación del proyecto
```

✅ **Ventajas de esta estructura:**  
- Facilita la escalabilidad.  
- Separa la lógica de negocio en archivos organizados.  
- Permite reutilización de código.  

---

## **8. Ejecutando la API con Uvicorn**  
Para poner en marcha la API, ejecutamos en la terminal:  
```bash
uvicorn main:app --reload
```
✔ `main` → Nombre del archivo (`main.py`).  
✔ `app` → Nombre de la instancia de FastAPI (`app = FastAPI()`).  
✔ `--reload` → Habilita recarga automática (ideal para desarrollo).  

### **Salida esperada en la terminal:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

### **📌 Probando la API**  
Abre tu navegador y visita **http://127.0.0.1:8000**.  
Verás una respuesta JSON como esta:  
```json
{
  "mensaje": "¡Hola, mundo! API funcionando correctamente"
}
```

✅ **Explora la documentación automática:**  
- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **Redoc UI** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

### 🎯 **Conclusión**  
- Instalamos **FastAPI y Uvicorn**.  
- Creamos nuestra primera **API con FastAPI**.  
- Aprendimos sobre la **estructura de proyectos**.  
- Ejecutamos la API y exploramos su **documentación automática**.  


----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------



# **Módulo 3: Creación de Rutas y Métodos HTTP en FastAPI**  

## **9. Métodos HTTP en FastAPI**  
Las APIs utilizan métodos HTTP para interactuar con los datos. Los principales son:  

| Método  | Descripción                        | Ejemplo en FastAPI |
|---------|------------------------------------|--------------------|
| `GET`   | Obtener datos                     | `@app.get("/")`   |
| `POST`  | Crear nuevos datos                | `@app.post("/")`  |
| `PUT`   | Actualizar datos existentes       | `@app.put("/")`   |
| `DELETE`| Eliminar datos                    | `@app.delete("/")`|

---

### **Ejemplo básico de cada método en FastAPI:**
```python
from fastapi import FastAPI

app = FastAPI()

# GET: Obtener un mensaje
@app.get("/")
def obtener_mensaje():
    return {"mensaje": "Este es un mensaje GET"}

# POST: Crear un nuevo mensaje
@app.post("/")
def crear_mensaje():
    return {"mensaje": "Mensaje creado con POST"}

# PUT: Actualizar un mensaje existente
@app.put("/")
def actualizar_mensaje():
    return {"mensaje": "Mensaje actualizado con PUT"}

# DELETE: Eliminar un mensaje
@app.delete("/")
def eliminar_mensaje():
    return {"mensaje": "Mensaje eliminado con DELETE"}
```

---

## **10. Parámetros en las Rutas**  
FastAPI permite definir **parámetros en las rutas** para manejar datos dinámicos.  

### **Ejemplo de ruta con parámetros**  
```python
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "nombre": "Carlos"}
```
📌 **Explicación:**  
- `{usuario_id}` es un **parámetro de ruta**.  
- FastAPI convierte automáticamente `usuario_id` a un **entero (`int`)**.  
- Devuelve un JSON con el ID y un nombre ficticio.  

🔹 **Prueba la API en el navegador:**  
Visita: [http://127.0.0.1:8000/usuarios/5](http://127.0.0.1:8000/usuarios/5)  

🔹 **Respuesta esperada:**  
```json
{
  "usuario_id": 5,
  "nombre": "Carlos"
}
```

---

## **11. Query Parameters y Request Body**  

### **🟢 Query Parameters**  
Los **Query Parameters** permiten enviar datos en la URL, por ejemplo:  
`http://127.0.0.1:8000/productos?categoria=electronica&precio_max=500`

📌 **Ejemplo en FastAPI:**  
```python
@app.get("/productos")
def obtener_productos(categoria: str, precio_max: int):
    return {"categoria": categoria, "precio_max": precio_max}
```
🔹 **Prueba la API en el navegador:**  
[http://127.0.0.1:8000/productos?categoria=ropa&precio_max=200](http://127.0.0.1:8000/productos?categoria=ropa&precio_max=200)  

🔹 **Salida esperada:**  
```json
{
  "categoria": "ropa",
  "precio_max": 200
}
```

---

### **🟢 Request Body (Cuerpo de la Solicitud)**  
Cuando usamos **POST o PUT**, enviamos datos en el **cuerpo de la solicitud** en formato JSON.  

📌 **Ejemplo con `Request Body` en FastAPI:**  
```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {"mensaje": "Usuario creado", "usuario": usuario}
```
🔹 **Cómo probarlo:**  
1. Ir a **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
2. Seleccionar **POST /usuarios**.  
3. Enviar un JSON como este:  
```json
{
  "nombre": "Juan",
  "edad": 30,
  "email": "juan@example.com"
}
```
🔹 **Salida esperada:**  
```json
{
  "mensaje": "Usuario creado",
  "usuario": {
    "nombre": "Juan",
    "edad": 30,
    "email": "juan@example.com"
  }
}
```

---

## **12. Validación de Datos con Pydantic**  
FastAPI usa **Pydantic** para validar datos automáticamente.  

📌 **Ejemplo con validaciones:**  
```python
class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str

    @validator("edad")
    def validar_edad(cls, edad):
        if edad < 18:
            raise ValueError("La edad debe ser mayor o igual a 18")
        return edad
```
🔹 Si enviamos un usuario con edad **menor a 18**, la API devuelve un error 422:  
```json
{
  "detail": [
    {
      "loc": ["body", "edad"],
      "msg": "La edad debe ser mayor o igual a 18",
      "type": "value_error"
    }
  ]
}
```

---

### 🎯 **Conclusión**  
- FastAPI permite definir rutas con **GET, POST, PUT y DELETE**.  
- Podemos usar **parámetros de ruta y query parameters** para recibir datos en la URL.  
- Con **Request Body y Pydantic**, validamos datos enviados en JSON.  



----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------





# **Módulo 4: Manejo de Datos en FastAPI**  

## **13. Conectando FastAPI con una Base de Datos (SQLite, PostgreSQL o MongoDB)**  

FastAPI admite múltiples bases de datos, pero las más comunes son:  
- **SQLite**: Base de datos liviana y fácil de usar.  
- **PostgreSQL**: Base de datos robusta y escalable para entornos de producción.  
- **MongoDB**: Base de datos NoSQL flexible para datos sin estructura fija.  

---

### **13.1 Instalando SQLAlchemy y Configurando la Base de Datos**  

📌 **Instalamos SQLAlchemy y el driver de PostgreSQL:**  
```bash
pip install sqlalchemy psycopg2
```
Para SQLite, solo necesitas instalar SQLAlchemy.  

📌 **Creamos `database.py` para gestionar la conexión:**  
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Para PostgreSQL: "postgresql://usuario:password@localhost/nombre_db"
DATABASE_URL = "sqlite:///./test.db"  # Usaremos SQLite en este ejemplo

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```
🔹 **Este código crea la conexión a la base de datos y define `SessionLocal` para manejar sesiones.**  

---

## **14. CRUD en FastAPI: Crear, Leer, Actualizar y Eliminar registros**  

CRUD significa:  
- **C**reate (Crear)  
- **R**ead (Leer)  
- **U**pdate (Actualizar)  
- **D**elete (Eliminar)  

📌 **Definimos un modelo en `models.py`:**  
```python
from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```
🔹 **Este modelo define una tabla `usuarios` en la base de datos.**  

📌 **Creamos la tabla ejecutando:**  
```python
from .database import engine, Base

Base.metadata.create_all(bind=engine)
```
---

### **14.1 Creando la API para CRUD**  

📌 **Creamos `schemas.py` para definir los esquemas de entrada y salida:**  
```python
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    pass  # No necesita campos adicionales para la creación

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
```
🔹 **Estos esquemas validan los datos recibidos en la API.**  

📌 **Creamos `crud.py` para manejar las operaciones en la base de datos:**  
```python
from sqlalchemy.orm import Session
from . import models, schemas

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    nuevo_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario
```
---

### **14.2 Implementando las Rutas CRUD en `main.py`**  

📌 **Importamos las dependencias necesarias:**  
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud

app = FastAPI()

# Dependencia para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

📌 **Creamos las rutas CRUD:**  

✔ **Obtener todos los usuarios:**  
```python
@app.get("/usuarios/", response_model=list[schemas.UsuarioResponse])
def leer_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)
```

✔ **Obtener un usuario por ID:**  
```python
@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioResponse)
def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.obtener_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
```

✔ **Crear un usuario:**  
```python
@app.post("/usuarios/", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)
```

✔ **Eliminar un usuario:**  
```python
@app.delete("/usuarios/{usuario_id}")
def borrar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.eliminar_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
```

🔹 **Ahora podemos probar nuestra API con Swagger UI en:**  
👉 `http://127.0.0.1:8000/docs`

---

## **15. Dependencias en FastAPI: Uso avanzado de `Depends()`**  

Las dependencias en FastAPI permiten reutilizar código en múltiples rutas.  

📌 **Ejemplo de dependencia para validar que un usuario tenga un email válido:**  
```python
from fastapi import Query

def validar_email(email: str = Query(..., regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$")):
    return email
```

📌 **Usamos esta dependencia en la creación de usuarios:**  
```python
@app.post("/usuarios/")
def crear_usuario(nombre: str, email: str = Depends(validar_email), db: Session = Depends(get_db)):
    usuario = schemas.UsuarioCreate(nombre=nombre, email=email)
    return crud.crear_usuario(db, usuario)
```
🔹 **Si se ingresa un email inválido, la API rechazará la solicitud.**  

---

### 🎯 **Conclusión**  
✔ **Conectamos FastAPI con SQLite/PostgreSQL.**  
✔ **Implementamos CRUD (Crear, Leer, Actualizar, Eliminar).**  
✔ **Aprendimos sobre dependencias en FastAPI (`Depends()`).**  



----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------



# **Módulo 5: Seguridad y Autenticación en FastAPI**  

## **16. Autenticación con OAuth2 y JWT**  

### **16.1 ¿Qué es OAuth2 y JWT?**  
- **OAuth2**: Un estándar de autenticación para permitir el acceso seguro a recursos protegidos.  
- **JWT (JSON Web Token)**: Un token en formato JSON que se usa para identificar usuarios de manera segura.  

📌 **Instalamos las librerías necesarias:**  
```bash
pip install python-jose[cryptography] passlib bcrypt
```

---

### **16.2 Creando el Sistema de Autenticación**  

📌 **Configuramos JWT en `auth.py`:**  
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Clave secreta y algoritmo para JWT
SECRET_KEY = "supersecreto"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generar_password_hash(password):
    return pwd_context.hash(password)

def crear_token_jwt(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```
🔹 **Este código nos permite encriptar contraseñas y generar tokens JWT.**  

📌 **Modificamos el modelo de usuario en `models.py` para incluir la contraseña:**  
```python
from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
```

📌 **Modificamos el registro de usuarios en `main.py`:**  
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, auth, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registro/")
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    hashed_password = auth.generar_password_hash(usuario.password)
    nuevo_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email, hashed_password=hashed_password)

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return {"mensaje": "Usuario registrado exitosamente"}
```
🔹 **Ahora almacenamos las contraseñas de forma segura.**  

---

### **16.3 Creando el Endpoint de Login con JWT**  

📌 **Agregamos un endpoint de login en `main.py`:**  
```python
from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()

    if not usuario or not auth.verificar_password(form_data.password, usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = auth.crear_token_jwt({"sub": usuario.email})

    return {"access_token": access_token, "token_type": "bearer"}
```
🔹 **Ahora los usuarios pueden autenticarse y recibir un token JWT.**  

Ejemplo de respuesta:  
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

## **17. Manejo de Usuarios y Permisos**  

📌 **Creamos una función para obtener el usuario desde el token JWT:**  
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def obtener_usuario_desde_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
```
🔹 **Esta función decodifica el token JWT y extrae el email del usuario.**  

📌 **Protegemos una ruta con autenticación:**  
```python
@app.get("/perfil/")
def obtener_perfil(usuario_email: str = Depends(obtener_usuario_desde_token), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
```
🔹 **Solo los usuarios autenticados pueden acceder a `/perfil/`.**  

---

## **18. Middleware en FastAPI: Protección de Rutas**  

Un **middleware** es una función que se ejecuta antes de cada solicitud.  

📌 **Creamos un middleware en `middleware.py` para registrar todas las peticiones:**  
```python
from fastapi import Request
from fastapi.responses import JSONResponse
import time

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} completado en {process_time:.2f} seg")
    return response
```
📌 **Lo agregamos en `main.py`:**  
```python
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.middleware("http")(log_requests)
```
🔹 **Este middleware registrará todas las peticiones a la API.**  

---

### 🎯 **Conclusión**  
✔ **Implementamos autenticación con OAuth2 y JWT.**  
✔ **Protegimos rutas y creamos un sistema de permisos.**  
✔ **Usamos middleware para registrar peticiones.**  


----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------


# **Módulo 6: Documentación y Despliegue en FastAPI**  

## **19. Documentación Automática con Swagger y Redoc**  

FastAPI genera automáticamente una documentación interactiva para nuestra API.  

📌 **Accedemos a la documentación en:**  
- **Swagger UI:** `http://127.0.0.1:8000/docs`  
- **ReDoc:** `http://127.0.0.1:8000/redoc`  

📌 **Podemos personalizar el título y descripción en `main.py`:**  
```python
from fastapi import FastAPI

app = FastAPI(
    title="Mi API con FastAPI",
    description="Una API de ejemplo utilizando FastAPI.",
    version="1.0.0",
    contact={
        "name": "Tu Nombre",
        "email": "tucorreo@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
```
🔹 **Esto personaliza la documentación en Swagger y Redoc.**  

📌 **Agregamos descripciones a los endpoints:**  
```python
@app.get("/usuarios/", summary="Obtener todos los usuarios", description="Devuelve una lista con todos los usuarios registrados.")
def leer_usuarios():
    return [{"id": 1, "nombre": "Juan"}]
```
🔹 **Ahora la documentación incluirá descripciones detalladas de cada ruta.**  

---

## **20. Desplegando una API con FastAPI en Heroku o AWS**  

### **20.1 Configuración para Despliegue**  

📌 **Creamos el archivo `requirements.txt` con las dependencias:**  
```bash
pip freeze > requirements.txt
```

📌 **Creamos `Procfile` para ejecutar la API en producción:**  
```
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000}
```

---

### **20.2 Desplegar en Heroku**  

📌 **1. Instalamos la CLI de Heroku y nos autenticamos:**  
```bash
heroku login
```

📌 **2. Creamos un nuevo proyecto en Heroku:**  
```bash
heroku create mi-api-fastapi
```

📌 **3. Subimos el código a Heroku:**  
```bash
git init
git add .
git commit -m "Primer despliegue"
heroku git:remote -a mi-api-fastapi
git push heroku main
```

📌 **4. Accedemos a nuestra API en:**  
```
https://mi-api-fastapi.herokuapp.com/docs
```

---

### **20.3 Desplegar en AWS con EC2**  

📌 **1. Creamos una instancia EC2 en AWS.**  
📌 **2. Instalamos Python y Uvicorn:**  
```bash
sudo apt update
sudo apt install python3-pip
pip install fastapi uvicorn
```
📌 **3. Ejecutamos la API en el servidor:**  
```bash
uvicorn main:app --host=0.0.0.0 --port=8000
```

📌 **4. Configuramos el firewall para permitir tráfico en el puerto 8000.**  

---

## **21. Buenas Prácticas para Producción**  

📌 **1. Seguridad: Uso de HTTPS y CORS**  
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
🔹 **Esto protege nuestra API de ataques de CORS.**  

---

📌 **2. Manejo de Logs en Producción**  
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/log/")
def generar_log():
    logger.info("Endpoint /log/ llamado")
    return {"mensaje": "Log registrado"}
```
🔹 **Esto guarda registros de las peticiones a nuestra API.**  

---

📌 **3. Monitoreo con Prometheus**  
Podemos usar **Prometheus y Grafana** para monitorear el rendimiento de la API.  

📌 **Instalamos Prometheus FastAPI Instrumentator:**  
```bash
pip install prometheus-fastapi-instrumentator
```
📌 **Lo agregamos en `main.py`:**  
```python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```
🔹 **Ahora podemos monitorear métricas en `/metrics`.**  

---

### 🎯 **Conclusión**  
✔ **Generamos documentación automática con Swagger y Redoc.**  
✔ **Desplegamos la API en Heroku y AWS.**  
✔ **Aplicamos buenas prácticas de seguridad, logs y monitoreo.**  
