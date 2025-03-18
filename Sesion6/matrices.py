#Listas
"""
persona = []

print(persona)
persona.append("Carlos")
persona.append(20)


carro = []

print(carro)
carro.append("Toyota")
carro.append(2010)

print (f"Persona:, {persona}")
print(f"Carro:, {carro}")
print(type(persona))
print(type(carro))
"""
#Tupla 

"""libros = ("Romanticos", "Aventura", "Ciencia Ficcion", "Fantasia")
frutas = ("Manzana", "Pera", "Uva", "Mango")


print(libros)
print(frutas)

print(type(libros))
print(type(frutas))

#Convertir tuplas a listas
listaLibros = list(libros)
listafrutas = list(frutas)

print(listaLibros)
print(listafrutas)
print(type(listaLibros))
print(type(listafrutas))"""

#Conjuntos / Sets

"""persona = {"Carlos", 20, "Calle 1", 1234567}
print(persona)
print(type(persona))

persona.add(1.78)
print(persona)"""

#Diccionarios


'''
print(type(persona))
print(persona)
print(persona["nombre"], persona["edad"])
personad = (persona.get("direccion"))
print(persona.get("nombre"))
'''

# for i, v in enumerate(persona):
#     print(f"La llave es: {i} y el valor es: {v}")

# print(persona.keys())
# print(persona.values())
# print(persona.items())

persona = {
    "nombre": "Carlos",
    "edad": 20,
    "direccion": "Calle 1",
    "Edad": 20,
    "telefono": 1234567
}

print(persona)
persona.update({"Trabajo": "Programador"})
print(persona)

persona["Padre de Familia"] = False
print(persona)

del persona["Edad"]
print(persona)

persona.pop("telefono")
print(persona)