# Evaluacion_T5
# Ejercicio 1 (2 Puntos)
Crea el siguiente módulo:

·        El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una división entres dos números. Todas ellas devolverán el resultado.

·        En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:

·        TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.

·        ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.

Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:

from operaciones import *

 

a, b, c, d = (10, 5, 0, "Hola")

 

print( "{} + {} = {}".format(a, b, suma(a, b) ) )

print( "{} - {} = {}".format(b, d, resta(b, d) ) )

print( "{} * {} = {}".format(b, b, producto(b, b) ) )

print( "{} / {} = {}".format(a, c, division(a, c) ) )


# Ejercicio 2 (3 Puntos)
En este ejercicio deberás crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt que almacenará un contador de visitas (será un número):

·        Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.

·        Luego a partir de un argumento:

·        Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.

·        Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.

·        Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.

·        Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.

·        Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.

# Ejercicio 3 (3 Puntos)
Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes gestor.py para añadir y borrar la información de los siguientes personajes:

Vida

Ataque

Defensa

Alcance

Caballero

4

2

4

2

Guerrero

2

4

2

4

Arquero

2

4

1

8

Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.

·        Crea dos clases, una Personaje y otra Gestor.

·        La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).

·        Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos y borrarlos (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente.

·        En caso de que el personaje ya exista en el Gestor entonces no se creará.

Una vez lo tengas listo realiza las siguientes prueba en tu código:

·        Crea los tres personajes de la tabla anterior y añádelos al Gestor.

·        Muestra los personajes del Gestor.

·        Borra al Arquero.

·        Muestra de nuevo el Gestor.

Sugerencia

El ejemplo con pickle que realizamos anteriormente puede servirte como base.

# Ejercicio 4 (2 Puntos)
¿Eres capaz de desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual? Hazlo en un script llamado reloj.py y ejecútalo en la terminal:

Ayuda

El módulo time integra una función llamada sleep(segundos) que puede pausar la ejecución de un programa durante un tiempo. Así mismo el módulo os integra la función system('cls') y system('clear') para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respecticamente.

