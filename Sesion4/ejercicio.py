menu = print("Menú\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
n = int(input("Introduce un número de Menú: "))
while n != 5:
    if n == 1:
        print("Has elegido la opción de Suma")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("La suma de los números es: ", a + b)
    elif n == 2:
        print("Has elegido la opción de Resta")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: ")) 
        print("La RESTA de los números es: ", a - b)
    elif n == 3:
        print("Has elegido la opción de Multiplicación")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número:"))
        print("La MULTIPLICACIÓN de los números es: ", a * b)
    elif n == 4:
        print("Has elegido la opción de División")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("La DIVISIÓN de los números es: ", a / b)
    elif n == 5:
        print("Saliendo del programa")
        break 
    else:
        print("Introduce un número de Menú válido")
        
    
