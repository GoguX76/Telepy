import telebot as tl #Importo la libreria para manejar al bot de Telegram.
import requests as rq 
from bot.config import TELEGRAM_TOKEN, API_URL

usuarios_bot = tl.TeleBot(TELEGRAM_TOKEN) #Creo el bot mediante el token que Telegram te da al crea el bot.

#Función que se ejecuta al momento que el usuario escriba el comando '/start' y muestra el mensaje el pantalla descrito.
@usuarios_bot.message_handler(commands=['start'])
def start(message):
    usuarios_bot.reply_to(
        message,
        "¡Hola!\n\n"
        "Soy un bot para gestionar los usuarios presentes en el sistema\n"
        "Usa /help para ver los comandos disponibles"
    )

#Función que se ejecuta al momento que el usuario escriba el comando 'help', que le da orientación al usuario de que comandos puede utilizar.
@usuarios_bot.message_handler(commands=['help'])
def help_command(message):
    usuarios_bot.reply_to(
        message,
        "Comandos Disponibles\n\n"
        "/start - Iniciar el bot\n"
        "/help - Ver esta ayuda\n"
        "/registrar - Registras a un usuario"
        "/mostrar - Muestra a todos los usuarios en el sistema.",
        parse_mode='Markdown'
    )

#Conjunto de funciones que llaman a las APIs para crear al usuario mediante al bot de Telegram con el comando '/registrar'
@usuarios_bot.message_handler(commands=['registrar'])
def registrar_usuario(message):
    msg = usuarios_bot.reply_to(message, "Ingrese su nombre:") #Le pide al usuario que ingrese el nombre.
    usuarios_bot.register_next_step_handler(msg, procesar_nombre) #Espera la respuesta del usuario para continuar y ejecutar las siguientes funciones.

def procesar_nombre(message):
    nombre = message.text.capitalize() #Transforma el String de nombre para que el primer carácter este en mayúsculas
    msg = usuarios_bot.reply_to(message, "Ingrese su edad:") #Le pide al usuario que ingrese la edad.
    usuarios_bot.register_next_step_handler(msg, procesar_edad, nombre) #Espera la respuesta del usuario para continuar y ejecutar las siguientes funciones.

def procesar_edad(message, nombre):
    edad = message.text #Le da el valor del último mensaje que se le escribió al bot, que en este caso fue la edad
    msg = usuarios_bot.reply_to(message, "Ingrese su género (M/F):") #Le pide al usuario que ingrese el genero.
    usuarios_bot.register_next_step_handler(msg, procesar_genero, nombre, edad) #Espera la respuesta del usuario para continuar y ejecutar las siguientes funciones.

def procesar_genero(message, nombre, edad):
    genero = message.text.upper() #Le da el valor del último mensaje que se le escribió al bot, que en este caso fue el genero.

    # Ingresa los datos a un diccionario que se le entregara a la API.
    data = {
        "Nombre": nombre,
        "Edad": edad,
        "Genero": genero
    }

    try:
        response = rq.post(f"{API_URL}/usuarios/registrar", json=data) #Ingresa los valores a la ruta API con el método POST.

        if response.status_code == 200: #Comprueba que la respuesta fue correcta.
            result = response.json() #Obtiene el JSON de la API.
            usuario = result['usuario'] #La variable usuario almacena el resultado del JSON con los valores de usuarios.

            #El bot devuelve una respuesta con los datos del usuario creado.
            usuarios_bot.reply_to(
                message,
                f"✅ Usuario registrado exitosamente!\n\n"
                f"ID: {usuario['id']}\n"
                f"Nombre: {usuario['Nombre']}\n"
                f"Edad: {usuario['Edad']}\n"
                f"Género: {usuario['Genero']}"
            )
        #En caso de errores, el bot se los muestra al usuario.
        else:
            error = response.json()
            usuarios_bot.reply_to(message, f"Error: {error['detail']}")
    except Exception as e:
        usuarios_bot.reply_to(message, f"Error al conectarse a la API. {str(e)}")

#Función que devuelve la lista de usuarios a través del bot de Telegram mediante el comando '/mostrar'.
@usuarios_bot.message_handler(commands=['mostrar'])
def mostrar_usuarios(message):
    try:
        response = rq.get(f"{API_URL}/usuarios") #Obtiene los datos de la ruta API mediante el método GET.

        if response.status_code == 200: #Comprueba de que la conexión a la API fue correcta.
            result = response.json() #Obtiene el JSON de la API
            usuario = result['usuarios'] #La variable usuario almacena el resultado del JSON con los valores de usuarios.
            total = result['total'] #La variable total almacena el resultado del JSON con el valor de total.
            mensaje = f"Total de usuarios: {total}\n\n" #Crea una variable que será el mensaje que mostrará el bot.

            #Recorrido con for en usuario para mostrar todos los usuarios en el sistema con un formato ordenado, sumando los resultados a la variable antes definida.
            for usuario in usuario:
                mensaje += f"Usuarios totales en el sistema: {total}\n"
                mensaje += f"ID: {usuario['id']}\n"
                mensaje += f"Nombre: {usuario['Nombre']}\n"
                mensaje += f"Edad: {usuario['Edad']}\n"
                mensaje += f"Género: {usuario['Genero']}"
                mensaje += "─" * 30 + "\n"
            usuarios_bot.reply_to(message, mensaje) #Muestra el mensaje con todos los usuarios.
        #En caso de errores, el bot se los muestra al usuario.
        else:
            error = response.json() 
            usuarios_bot.reply_to(message, f"Error: {error['detail']}")
    except Exception as e:
        usuarios_bot.reply_to(message, f"Error al conectarse a la API: {e}")
