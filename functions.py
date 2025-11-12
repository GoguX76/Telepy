from fastapi import HTTPException
import requests as rq
import random as rd
import uvicorn
import time as tm

API_URL = "http://localhost:8000" #Variable que tendra el valor del localhost para manejar las rutas apis.

#Función que verifica si la api se está ejecutando.
def verificar_api():
    try:
        response = rq.get(f"{API_URL}", timeout=2) #Trata de obtener respuesta de la api para confirmar si ya está encendida.
        return response.status_code == 200 #Si la api devuelve una respuesta, se envía el código 200.
    except:
        return False #Si no devuelve nada, retorna False
    
def iniciar_api():
    import threading as th

    #Función que ejecuta el comando para iniciar la API.
    def run_api():
        uvicorn.run("api-usuarios:app", host="127.0.0.1", port=8000, log_level="info")

    api_thread = th.Thread(target=run_api, daemon=True) #Ejecuta un hilo donde ejecutará la función de iniciar la API.
    api_thread.start() #Se ejecuta el Hilo.

    print("Iniciando API...")
    for i in range(10):
        tm.sleep(1)

        #Verifica si la API ha devuelto una respuesta
        if verificar_api():
             print("API iniciada correctamente")
             return True
        else:
            print(f"Esperando...({i+1}/10)")

    print("No se pudo iniciar la API")
    return False

#Función que crea un usuario en el sistema mediante las apis creadas.
def crear_usuario_api():
    print("Para empezar, ingrese su nombre de usuario")
    nom = input(">> ")

    print("Ahora, ingrese su edad")
    age = input(">> ")

    print("Por último, indique su genero")
    gender = input(">> ").upper()

    data = {
        "Nombre": nom,
        "Edad": age,
        "Genero": gender
    }

    response = rq.post(f"{API_URL}/usuarios/registrar", json=data) #POST es para añadir un dato al sistema con la ruta API definida en el módulo api-usuarios.

    #Verifica que el usuario haya sido registrado correctamente.
    if response.status_code == 200:
        result = response.json()
        usuario = result['usuario']

        print("El usuario ha sido registrado con éxito")
        print(f"ID generado: {usuario['id']}")
    else:
        print(f"Error: {response.json()}")

#Función que muestra a los usuarios que hay en el sistema mediante la api.
def mostrar_usuarios_api():
    response = rq.get(f"{API_URL}/usuarios")

    #Verifica que hayan usuarios dentro del sistema.
    if response.status_code == 200:
        data = response.json()
        usuarios = data["usuarios"]

        if not usuarios:
            print("No se han encontrado usuarios en el sistema")
            return

        #Muestra a los usuarios que hay en el sistema.
        print(f"=== TOTAL USUARIOS: {data['total']} ===\n")
        
        for usuario in usuarios:
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Edad: {usuario['Edad']}")
            print(f"Genero: {usuario['Genero']}")
            print("-" * 40)

    else:
        print(f"Error al obtener a los usuarios")

#Función que permite buscar un usuario mediante su id.
def buscar_usuario_id():
    print("Ingrese el ID del usuario del que desea saber sus datos")

    try:
        user_id = int(input(">> "))
    except ValueError:
        print("Error: El ID debe ser un número")
        return

    response = rq.get(f"{API_URL}/usuarios/{user_id}")

    #Verifica que el usuario haya sido encontrado y muestra sus datos.
    if response.status_code == 200:
        data = response.json()
        usuario = data['usuario']

        print("\n=== USUARIO ENCONTRADO ===")
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['Nombre']}")
        print(f"Edad: {usuario['Edad']}")
        print(f"Genero: {usuario['Genero']}")
        print("-" * 40)

    else:
        print("El usuario no ha sido encontrado")

#Función que permite actualizar los datos de un usuario mediante su id.
def actualizar_usuario_api():
    print("Ingrese el ID del usuario del que desea actualizar sus datos")
    
    #Evalua que se ingrese la ID como int.
    try:
        user_id = int(input(">> "))
    except ValueError:
        print("Error: El ID debe ser un número")
        return

    response_check = rq.get(f"{API_URL}/usuarios/{user_id}") #GET permite recoger los datos de la ruta API.

    #Si no encuentra el usuario, devuelve error.
    if response_check.status_code == 404:
        print(f"Error: No existe el usuario en el sistema")
        return

    print("\n=== INGRESE LOS NUEVOS DATOS ===\n")
    print("Ingrese el nuevo nombre de usuario")
    nom = input(">> ")

    print("Ingrese la nueva edad")
    age = input(">> ")

    print("Ingrese el nuevo genero")
    gender = input(">> ").upper()

    data = {
        "Nombre": nom,
        "Edad": age,
        "Genero": gender
    }

    response = rq.put(f"{API_URL}/usuarios/actualizar/{user_id}", json=data) #PUT permite modificar datos ya en el sistema.

    #Verifica que los datos del usuario se hayan actualizado correctamente.
    if response.status_code == 200:
        print("El usuario ha sido actualizado exitosamente")
    else:
        error = response.json()
        print(f"Error al actualizar al usuario: {error['detail']}")


#Función que muestra el menú para que el usuario pruebe la api.
def mostrar_menu():
    print("=" * 40)
    print("=== SISTEMA DE GESTIÓN DE USUARIOS === ")
    print("=" * 40)
    print("1. Registrar un usuario en el sistema")
    print("2. Mostrar todos los usuarios en el sistema")
    print("3. Buscar usuario mediante su ID")
    print("4. Actualizar datos de usuario mediante su ID")
    print("5. Salir")

#Función que maneja las funciones que llaman a las apis.
def main():
    print("¡Bienvenido al sistema de gestión de usuarios!")
    print("Este sistema es parte de estudio para el evento Bothaton")

    #Antes de mostrar el menu, se verifica que la API este corriendo.
    if verificar_api():
        print("La API ya está corriendo")
    else:
        print("La API no está corriendo")

        #Si la API no se logra iniciar, lanza error.
        if not iniciar_api():
            print("Error: No se pudo iniciar la API")
            print("Ejecuta la API manualmente en la terminal con: uvicorn api-usuarios:app --reload")
            return

    #Ejecuta el menu en un ciclo while y las funciones que llaman a las APIs.
    while True:
        mostrar_menu()
        print("\nElija una opción")
        opc = input(">> ")

        if opc == "1":
            crear_usuario_api()

        elif opc == "2":
            mostrar_usuarios_api()

        elif opc == "3":
            buscar_usuario_id()

        elif opc == "4":
            actualizar_usuario_api()

        elif opc == "5":
            print("Gracias por probar el sistema")
            break
        
        else:
            print("Opción inválida. Por favor, ingrese una opción dentro del menú")

        input("\nPresione Enter para continuar...")

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