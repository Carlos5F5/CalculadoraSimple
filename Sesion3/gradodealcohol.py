edad = int(input("Ingresa tu edad: "))
nivel_alcohol = float(input("Ingresa el nivel de alcohol en tu sangre (enmg/dL): "))

if edad >= 18:
    if nivel_alcohol < 0.05:
        print("Puedes conducir")
    else:
        print("No puedes conducir debido al alcohol en tu sangre")
else:
    print("No puedes conducir")