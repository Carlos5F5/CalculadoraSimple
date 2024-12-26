# Cree un archivo de python con el nombre taller1_ejercicio4.py

# El distrito metropolitano de Quito requiere un programa que solicite al usuario el ingreso de
# dos numeros diferentes y muestre en pantalla el mayor de los dos.

# Solicitar al usuario el ingreso de dos números diferentes
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Verificar si los números son iguales
while numero1 != numero2:
    if numero1 == numero2:
        print("Error: Los números ingresados son iguales. Deben ser diferentes.")
else:
    # Determinar y mostrar el mayor de los dos números
    if numero1 > numero2:
        print(f"El mayor de los dos números es: {numero1}")
    else:
        print(f"El mayor de los dos números es: {numero2}")



