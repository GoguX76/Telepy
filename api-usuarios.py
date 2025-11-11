from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions import validacionUsuario, validacionGenero, validacionEdad
import random as rd

app = FastAPI() #Creación de la aplicación para manejar las apis.

usuarios_sistema = [] #Lista que almacenará los usuarios registrados en el sistema.

#Creación de una clase Usuario para definir los datos que se usaran en este.
class Usuario(BaseModel):
    Nombre: str
    Edad: str
    Genero: str

#Genera una id de un número random y único.
def generar_id():
    while True:
        new_id = rd.randint(1, 9999)

        if not any(user["id"] == new_id for user in usuarios_sistema):
            return new_id

#Ruta API que corresponde a la raiz de todo el sistema.
@app.get("/")
def pag_raiz():
    return {"mensaje": "API de Usuarios Activa"}

#Ruta API que obtiene la información de todos los usuarios en el sistema.
@app.get("/usuarios")
def obtener_usuarios():
    return {
        "total": len(usuarios_sistema),
        "usuarios": usuarios_sistema
    }

#Ruta API que obtiene la información de el usuario con un id especifico.
@app.get("/usuarios/{id}")
def obtener_usuario_id(id: int):
    for usuario in usuarios_sistema:
        if usuario["id"] == id:
            return {
                "usuario": usuario
            }
    
    #El HTTPException es para lanzar un error en caso de que el codigo recibido sea x con un mensaje detallado.
    raise HTTPException(
        status_code=404,
        detail=f"El usuario con id {id} no ha sido encontrado en el sistema"
    )

#Ruta API que permite registrar un usuario al sistema con el método POST.
@app.post("/usuarios/registrar")
def registrar_usuarios(usuario: Usuario):
    if not validacionUsuario(usuario.Nombre):
        raise HTTPException(status_code=400, detail="Nombre inválido")
    
    if not validacionEdad(usuario.Edad):
        raise HTTPException(status_code=400, detail="Edad inválida")
    
    if not validacionGenero(usuario.Genero):
        raise HTTPException(status_code=400, detail="Genero inválido")

    genero_completo = "Masculino" if usuario.Genero == "M" else "Femenino"

    #Ingresa al nuevo usuario con los datos dados.
    new_user = {
        "id": generar_id(),
        "Nombre": usuario.Nombre,
        "Edad": usuario.Edad,
        "Genero": genero_completo
    }

    usuarios_sistema.append(new_user) #Aquí los agrega a la lista donde van todos los usuarios.

    return {
        "mensaje": "¡El usuario ha sido registrado de manera exitosa!"
    }

@app.put("usuarios/actualizar/{id}")
def actualizar_usuario(usuario: Usuario, id: int):
    for i, usuario in enumerate(usuarios_sistema,1):
        if usuario['id'] == id:
            if not validacionUsuario(usuario.Nombre):
                raise HTTPException(status_code=400, detail="Nombre inválido")
            
            if not validacionEdad(usuario.Edad):
                raise HTTPException(status_code=400, detail="Edad inválida")
            
            if not validacionGenero(usuario.Genero):
                raise HTTPException(status_code=400, detail="Genero inválido")

            genero_completo = "Masculino" if usuario.Genero == "M" else "Femenino"

            usuarios_sistema[i] = {
                "id": id,
                "Nombre": usuario.Nombre,
                "Edad": usuario.Edad,
                "Genero": genero_completo
            }

            return {
                "mensaje": "Los datos del usuario han sido actualizados correctamente"
            }
    raise HTTPException(
        status_code = 404,
        detail = "El usuario no ha sido encontrado en el sistema"
    )