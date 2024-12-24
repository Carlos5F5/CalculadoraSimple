nombre = str(input("Ingresa tu nombre: "))

calculadora = "Ok " + nombre+  " Escoge una operación: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n"
print(calculadora)
opcion = int(input("Opción: "))

while opcion != 5:
    if opcion == 1:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        print(f"Resultado: {num1 + num2}")
    elif opcion == 2:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {num1 - num2}")
    elif opcion == 3:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {num1 * num2}")
    elif opcion == 4:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {num1 / num2}")
    elif opcion == 5:
        print("Adiós")
    else:
        print("Opción no válida, intenta de nuevo")
 
    break
