num1 = int(input("Número 1: "))
num2 = float(input("Número 2: "))
res = num1 + num2
print("El valor 1 es: ", num1, "su tipo es: ", type(num1))
print("El valor 2 es: ", num2, "su tipo es: ", type(num2))

print("La suma de los dos valores es: ", res, "su tipo es: ", type(res))

if res == 25:
    if type(res) == float():
        print("El resultado es un float")
        if type(res) != float():
            print("El resultado no es un float")
    else: 
         print("fin")
else:
        print("El resultado no es 25")

