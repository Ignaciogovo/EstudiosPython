from fastapi import FastAPI
app = FastAPI()
# Creamos una función
@app.get("/")

# Ejecutar servidor local: uvicorn main:app --reload

async def root():
    return "Hola mundo"

print(root())