"""palabra = "Feedback del for y while"

print(type(palabra))
print(len(palabra))

for i in palabra:
    print(i)
"""
n = int(input("Ingrese un número: "))
while n <= 5:
    print(n)
    if n == 3:
        print("El número es 3")
        break
    elif n < 5:
        print(n)
        n =+ 1
        continue
    
