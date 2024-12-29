num1 = int(input("Número 1: "))
num2 = float(input("Número 2: "))
res = num1 + num2
print("El valor 1 es: ", num1, "su tipo es: ", type(num1))
print("El valor 2 es: ", num2, "su tipo es: ", type(num2))

print("La suma de los dos valores es: ", res, "su tipo es: ", type(res))

if res == 25:
    print("El resultado de la suma es igual a 25")
elif res > 25:
        print("El resultado de la suma es mayor a 25")
else:
        print("El resultado de la suma es menor a 25")