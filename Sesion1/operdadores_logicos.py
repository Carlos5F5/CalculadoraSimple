"""
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

print(numero1 == numero2) #si son iguales es True, si no es False
print(numero1 != numero2) #si son diferentes es True, si no es False

print(numero1 > numero2) #si el primer número es mayor que el segundo es True, si no es False
print(numero1 >= numero2) #si el primer número es mayor o igual que el segundo es True, si no es False

print(numero1 < numero2) #si el primer número es menor que el segundo es True, si no es False
print(numero1 <= numero2) #si el primer número es menor o igual que el segundo es True, si no es False

print(numero1 > 5 and numero2 > 5) #si ambos números son mayores que 5 es True, si no es False
print(numero1 > 5 or numero2 > 5) #si alguno de los números es mayor que 5 es True, si no es False

print(not(numero1 > 5)) #si el número es mayor que 5 es False, si no es True

"""

#trabajando con listas


fruta1 = ["manzana", "pera", "uva", "sandía", "mango"]
fruta2 = ["manzana", "pera", "uva", "sandía", "mango"]
frutas = fruta1
print(fruta1 == fruta2) 

print("Contenido original: ",frutas)
frutas.append("naranja")
print("Usando el metodo append: ",frutas)

frutas.insert(2, "banano")
print("Usando el metodo insert: ",frutas)

frutas.remove("naranja")
print("Usando el metodo remove: ",frutas)

frutas.extend(["papaya", "piña"])
print("Usando el metodo extend: ",frutas)
