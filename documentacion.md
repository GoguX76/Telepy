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

## Notas Día 2
> Es mejor, para validar la edad, que se valide siendo esta un String, dependiendo de lo que se quiera hacer, y luego transformarla en un Int, como en mi caso, que primero valide si el campo estaba vacío y que no contuviera ninguna letra, ya que si fuera Int, sería un caso difícil. Luego de eso, ya transforme la edad a Int e hice las validaciones de rango de edad.