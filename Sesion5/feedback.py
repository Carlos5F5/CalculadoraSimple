#Trabajando con operaciones tipo CRUD

listaLibros = ["Romanticos", "Aventura", "Ciencia Ficcion", "Fantasia"]
print(listaLibros)
listaLibros.append("Drama")
listaLibros[0]
print(listaLibros)
#Actualizar
listaLibros[0] = "Terror"
print(listaLibros)
#Eliminar
listaLibros.remove("Fantasia")
print(listaLibros)