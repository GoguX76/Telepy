import requests as rq
import random as rd

API_URL = "http://localhost:8000"

def crear_usuario_api():
    print("Para empezar, ingrese su nombre de usuario")
    nom = input(">> ")

    print("Ahora, ingrese su edad")
    age = input(">> ")

    print("Por último, indique su genero")
    gender = input(">> ")

    data = {
        "Nombre": nom,
        "Edad": age,
        "Genero": gender
    }

    response = rq.post(f"{API_URL}/usuarios/registrar", json=data)

    if response.status_code == 200:
        print("El usuario ha sido registrado con éxito")
    else:
        print(f"Error: {response.json()}")

def mostrar_usuarios_api():
    response = rq.get(f"{API_URL}/usuarios")

    if response.status_code == 200:
        data = response.json()
        print(f"=== TOTAL USUARIOS: {len(data)} ===\n")
        
        for i, usuario in enumerate(data, 1):
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Edad: {usuario['Edad']}")
            print(f"Genero: {usuario['Genero']}")
            print("-" * 40)

    else:
        print(f"Error al obtener a los usuarios")

def buscar_usuario_id():
    print("Ingrese el ID del usuario del que desea saber sus datos")
    user_id = int(input(">> "))

    response = rq.get(f"{API_URL}/usuarios/{user_id}")

    if response.status_code == 200:
        user = response.json()
        for i, usuario in enumerate(user, 1):
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Edad: {usuario['Edad']}")
            print(f"Genero: {usuario['Genero']}")
            print("-" * 40)

    else:
        print("El usuario no ha sido encontrado")

def actualizar_usuario_api():
    print("Ingrese el ID del usuario del que desea actualizar sus datos")
    user_id = int(input(">> "))

    response_check = rq.get(f"")

    response = rq.put(f"{API_URL}/usuarios/actualizar/{user_id}")

    


#Función que valida que el usuario haya ingresado bien el nombre.
def validacionUsuario(nom):
    try:
        if not nom.strip(): #Con esto, compruebo que no hayan espacios ni caracteres dentro del nombre.
            raise ValueError("El campo de nombre no puede estar vacío.")
        
        if not nom.strip().isalpha(): #Con esto, compruebo que no hayan caracteres ni espacios, pero también que no haya números.
            raise ValueError("El nombre no puede contener números.")
        
        if len(nom) < 4: #Con esto, compruebo que la longitud del nombre sea mayor a 4 caracteres.
            raise ValueError("El nombre debe tener 4 carácteres como mínimo.")
        return True
    
    #En los excepts se manejan y muestran los errores definidos en los if de arriba.
    except TypeError as e:
        print(f"Error: {e}")
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
#Función que valida que el usuario haya ingresado bien la edad.
def validacionEdad(age):
    try:
        if not age.strip():
            raise ValueError("El campo de edad no puede estar vacío.")
        
        if any(c.isalpha() for c in age):
            raise ValueError("La edad no puede contener letras.")
        
        age_int = int(age)

        if age_int <= 0:
            raise ValueError("La edad no puede ser un numero negativo.")
        
        if age_int > 120:
            raise ValueError("La edad no puede ser mayor a 120 años.")
        
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
        return False

#Función que permite validar que el usuario haya ingresado bien su genero.
def validacionGenero(gender):
    try:
        if not gender.strip():
            raise ValueError("El campo de genero no puede estar vacío.")
        
        if not gender.strip().isalpha():
            raise ValueError("El genero no puede tener números.")
        
        if len(gender) > 1:
            raise ValueError("El genero solo puede tener un caracter (M/F).")
        
        if gender not in ["M", "F"]:
            raise ValueError("Ha ingresado un valor erroneo.")
        
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except TypeError as e:
        print(f"Error: {e}")
        return False