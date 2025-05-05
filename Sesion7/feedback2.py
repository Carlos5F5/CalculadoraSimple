def suma(n1, n2):
    r = n1 + n2
    return r

def resta(n1, n2):
    r = n1 - n2
    return r

def multiplicacion(n1, n2):
    r = n1 * n2 
    return r

""" try:
    num1 = int(input("Ingrese número 1: "))
    num2 = int(input("Ingrese número 2: "))

    rSuma = suma(num1, num2)
    print("El resultado de la suma es: ", rSuma)

    rResta = resta(num1, num2)
    print("El resultado de la resta es: ", rResta)

    rMultiplicacion = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es: ", rMultiplicacion)
    
except ValueError:
    print("Error: Ingrese solo números") """

while True:
    try:
        num1 = int(input("Ingrese número 1: "))
        num2 = int(input("Ingrese número 2: "))

        rSuma = suma(num1, num2)
        print("El resultado de la suma es: ", rSuma)

        rResta = resta(num1, num2)
        print("El resultado de la resta es: ", rResta)

        rMultiplicacion = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es: ", rMultiplicacion)
        break
    except ValueError:
            print("Error: Ingrese solo números. Inténtelo de nuevo.")