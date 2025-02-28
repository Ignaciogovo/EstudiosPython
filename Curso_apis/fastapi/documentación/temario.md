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

## Módulo 5: Seguridad y Autenticaciónw

- Autenticación con OAuth2 y JWT.
- Manejo de usuarios y permisos.
- Middleware en FastAPI: Protección de rutas.

## Módulo 6: Documentación y Despliegue

- Documentación automática con Swagger y Redoc.
- Desplegando una API con FastAPI: Opciones en servidores como Heroku o AWS.
- Buenas prácticas para producción: Seguridad, logs y monitoreo.





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
