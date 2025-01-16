"""materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nuevamateria = input("Ingrese una materia: ")
materias.append(nuevamateria)
print(materias)
"""

n = int(input("Ingrese el menu: "))
while n <=5:
    if n == 1:
        print("sumar", 2+2)
    elif n == 2:
        print("restar", 2-2)
    elif n == 3:
        print("multiplicar", 2*2)
    elif n == 4:
        print("dividir", 2/2)
    elif n == 5:
        print("salir")
        break