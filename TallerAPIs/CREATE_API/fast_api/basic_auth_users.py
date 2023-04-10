from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel # --> método de validación
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()

oauth2=OAuth2PasswordBearer(tokenUrl="login")

# POO
# entidad user:
class User(BaseModel):
    username: str
    full_name: str
    mail: str
    disabled: bool

class UserDB(BaseModel):
    password: str

users_db = {
    "moure" : 
    {
        "username": "moure",
        "full_name": "nombre moure",
        "mail": "moure@gmail.com",
        "disabled": False,
        "password": "654321"
    },
    "mourinho" : 
    {
        "username": "mourinho",
        "full_name": "mou fut",
        "mail": "mou@gmail.com",
        "disabled": True,
        "password": "321abc"
    }
}

def search_user(username: str):
    if username in users_db:
        # Añadimos a la clase UserDB los datos del json
        return UserDB(**users_db[username])

#### Esta función sera la dependencia de la función asincrona me del get("/user/me")
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales inválidas",headers={"WWW-Authenticate": "Bearer"})
    return token



@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db=users_db.get(form.username)
    if not user_db:
        # Realizar una excepción
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no es correcto")
    user = search_user(form.username)
    if not user.password==form.password:
        raise HTTPException(status_code=404,detail="La contraseña no es correcta")
    
    return{"access_token": form.username, "token_type": "bearer"}

@app.get("/user/me")
async def me(user: User=Depends(current_user)):
    return user
