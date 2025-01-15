datos = []
nombre =  input("Ingresa tu nombre: ")
Edad = int(input("Ingrese Edad: "))
estatura = float(input("Ingrese estatura: "))

datos.append(nombre)
datos.append(Edad)
datos.append(estatura)

print(datos)	
if Edad < 18:
    print("El menor de edad no puede beber cerverza")
else:
    print("Puedes beber cerverza")