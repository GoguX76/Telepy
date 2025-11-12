# Documentación practica Bothaton

En este repositorio, estaré almacenando todo lo que estaré practicando para el evento **Bothaton**, con el propósito de usarlo como retroalimentación y, tal como se llama este archivo, documentar todo lo que aprendo y hago en este repositorio hasta el día del evento.

## Avances

### Día 1 (09-11-2025)
- Implementé una validación para que el usuario ingrese bien su nombre y respete las reglas que yo mismo implemente, como que el nombre debe tener más de 4 caracteres.
- Aprendí para que sirve .strip() y .isalpha(), junto con como funcionan las condiciones if not.

## Notas Día 1
**.strip()** quita los espacios de un String, siendo conveniente para evitar cosas como " Juan ".

**.isalpha()** comprueba que, dentro de un String, todos los caracteres que se usen sean letras (a-z, A-Z), devoliendo **True**, y, en caso de que haya algún espacio, número o algo que no sea una letra, devuelve **False**

Los **if not** devuelven el resultado contrario o hacen la evaluación contraria, dependiendo lo que se quiere hacer. Por ejemplo, con **if not nom.strip()**, comprueba que, si después de quitar los espacios, el String sigue vacío, no devuelva False, sino que True, lo que permite cumplir la condición. Ahora, con **if not nom.isalpha()**, comprueba que **NO** haya ninguna letra dentro del String, y, al ser así, entra en el if y cumple la condición, todo esto visto en el archivo de functions.

### Día 2 (10-11-2025)
- Implementé dos funciones, una para validar que la edad que ingrese el usuario este bien y cumpla con las reglas del programa y otra que permite al usuario ingresar la edad.
- Utilize **any()** y aprendí como funciona la creación de **variables temporales** o **variables de iteración**.
- Implemente más funciones, las cuales validan y obtienen el genero que ingrese el usuario, mientras que las otras restantes registran a los usuarios a un diccionario, permitiendo también ver este mismo e ingresar varios usuarios al sistema, mostrándose estos de manera ordenada.
- Implemente y desarolle las **apis** para mi sistema, manejando ya las rutas para obtener usuarios, registrar usuarios y obtener usuarios mediante su id, junto a las validaciones ya hechas en el módulo de **functions** y con el manejo de errores con HTTPException.
- Elimine funciones en **functions** que ya no se utilizaban, ya que estaban siendo reemplazados por la api.

## Notas Día 2
Es mejor, para validar la edad, que se valide siendo esta un **String**, dependiendo de lo que se quiera hacer, y luego transformarla en un **Int**, como en mi caso, que primero valide si el campo estaba vacío y que no contuviera ninguna letra, ya que si fuera Int, sería un caso difícil. Luego de eso, ya transforme la edad a Int e hice las validaciones de rango de edad.

El **enumerate()** me permite recorrer datos de manera enumerada, como bien dice la función, recorriendo elementos uno por uno, siendo una manera eficiente de recorrer listas o diccionarios y, también, evitar usar el típico contador.

Se implementa la librería **FastAPI** para poder crear rutas api de manera rápida y sencilla. La aplicación de inicializa definiendo una variable como **FastAPI()** y, con esta misma variable, vas creando las diferentes rutas, lo que va a hacer esa ruta y los métodos que se van a utilizar en estas del **CRUD (Create, Read, Update, Delete)**.

El **HTMLException** funciona igual que el **raise ValueError**, en el sentido de que sirve para lanzar errores mediante cualquier excepción, solo que, con **HTMLException**, vas a proporcionar el código de error (Ej: 400), y luego un mensaje detallando el error, siendo similar que **raise ValueError** pero para las apis.

### Día 3 (11-11-2025 - 12-11-2025)
- Termine de implementar todas las funciones que utilizan el modulo de **api-usuarios.py** para que se puedan ejecutar en otro módulo, que en este caso es el **main.py**. Arreglo de varias de las funciones para que puedan funcionar bien con las APIs
- También corregí y añadi más métodos CRUD en el **api-usuarios.py**

## Notas Día 3
Es importante que, para cada acción que involucre añadir o actualizar un usuario, se debe crear un nuevo diccionario para luego añadirlos/actualizarlos en la lista donde se almacenan todos los usuarios. También, para estas mismas dos cosas y (creo), eliminar usuarios, devolver el usuario para que las funciones de **functions.py** sepan con que datos tienen que trabajar.

Revisar que siempre que los datos que se analicen sean los correctos.

Siempre recordar como definiste lo que devuelve una ruta (Tuve muchos errores por olvidarme de eso). También para comprender que es lo que quiere lograr y a los índices a los que se quieren acceder.