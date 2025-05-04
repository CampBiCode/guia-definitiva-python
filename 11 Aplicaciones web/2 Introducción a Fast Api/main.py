# Instalar FastAPI y Uvicorn
## pip install fastapi uvicorn



# Crear API

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saludo():
    return {"mensaje":"Hola mundo"}


@app.get("/elementos/{cantidad}")
def leer_elemento(cantidad: int, q: str = None):
    return [x for x in range(cantidad)]
## ejecutar aplicación
## uvicorn main:app --reload



# Crear CRUD de entidad usuario
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_db = []

class Usuario(BaseModel):
    id: int
    nombre: str
    edad: int
    profesion: str

# CREATE
@app.post("/usuarios/", response_model = Usuario)
def crear_usuario(usuario: Usuario):
    for db_usuario in fake_db:
        if db_usuario.id == usuario.id:
            raise HTTPException(status_code = 400, detail = "El usuario ya existe")
    fake_db.append(usuario)
    return usuario

# READ ALL
@app.get("/usuarios/", response_model = List[Usuario])
def leer_usuarios():
    return fake_db

# READ ONE
@app.get("/usuarios/{usuario_id}", response_model = Usuario)
def leer_usuario(usuario_id: int):
    for usuario in fake_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code = 404, detail = "Usuario no encontrado")

# UPDATE
@app.put("/usuarios/{usuario_id}", response_model = Usuario)
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for index, usuario in enumerate(fake_db):
        if usuario.id == usuario_id:
            fake_db[index] = usuario_actualizado
            return usuario_actualizado
    raise HTTPException(status_code = 404, detail = "Usuario no encontrado")

# DELETE
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for index, usuario in enumerate(fake_db):
        if usuario.id == usuario_id:
            del fake_db[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code = 404, detail = "Usuario no encontrado")