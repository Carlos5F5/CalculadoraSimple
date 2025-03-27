persona = ['Juan', 30, 1.80, "M"]
print("Elementos originales de la lista: ",persona)

persona.append("Soltero")
print("Lista modificada: ",persona)

persona.insert(1, "Quito")
print("Lista modificada: ",persona)

for  i, e in enumerate(persona):
    print(f"Posición {i}: {e}")

print("*********************")

for i, e in enumerate(persona):
    print(f"Posición {i}: {e}")