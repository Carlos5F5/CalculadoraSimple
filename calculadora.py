


def calculadora():
    print("Escoga una funcion")
    print("\n1. Sumar")
    print("\n2. Restar")
    print("\n3. Multiplicar")
    print("\n4. Dividir")
    opcion = int(input("\nDigite la opción: "))

    n1 = int(input("\n Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    while True:
        try:
            if opcion == 1:
                resultado = n1 + n2
                print(f"\nLa suma de {n1} + {n2} es: {resultado}")
            elif opcion == 2:
                resultado = n1 - n2
                print(f"\nLa resta de {n1} - {n2} es: {resultado}")
            elif opcion == 3:
                resultado = n1 * n2
                print("La multiplicación de", n1 * n2, "=", resultado) 
            elif opcion == 4:
                resultado = n1 / n2
                print (f"\nLa división de {n1} / {n2} es: {resultado}")
            else:
                print("\nOpción no válida")
        except ZeroDivisionError:
            print("\nNo se puede dividir entre cero")
        except ValueError:
            print ("Por favor ingrese una opcion válida")
        break

calculadora()

def repetiropciones():
    while True:
        try:
            print("\n¿Desea realizar otra operación?")
            print("\n1. Si")
            print("\n2. No")
            
            opcion1 = int(input("\nDigite la opción: "))

                 
            if opcion1 == 1:
                print (calculadora())
                print (repetiropciones())
            elif opcion1 == 2:
                print("\nGracias por usar la calculadora")
                
            else:
                print("\nOpción no válida")
            
        except ValueError:
            print ("Por favor ingrese una opcion válida")
        break    

repetiropciones()
# Fin del programa
