#Cree un archivo de python con el nombre taller1_ejercicio3.py

#1. Sabemos que la función input() captura lo que el usuario escribe en el programa, pero el tipo
#de dato que lee será siempre string. Si necesitamos que sea un número debemos convertir lo
#que input() captura. Para convertir a número entero usamos int(input()) y para convertir a
#número con decimales usamos float(input()).

#Sabiendo lo siguiente: El banco de Guayaquil solicita el desarrollo de un software para obtener la
#suma dos cantidades ingresadas por teclado.

#· El software evaluará si el resultado de la suma es mayor que 25 deberá mostrar el mensaje
#con el valor de la suma.
#. Además deberá mostrar un segundo mensaje que reste 5 al valor de la suma.
#· Si el resultado de la resta es menor que 10 que imprima por pantalla" Gracias por su visita,
#vuelva pronto."


cantidad1 = int(input("Ingrese la primera cantidad de dinero : "))
cantidad2 = int(input("Ingrese la segunda cantidad de dinero : "))
cantidad_total = cantidad1 + cantidad2
resta = cantidad_total - 5

if cantidad_total > 25:
    print("La cantidad total es: " , cantidad_total)
    print("La cantidad total menos 5 es: " , resta)
elif resta < 10:
    print("La cantidad total eres pobre")

    