#Trabajando con operaciones tipo CRUD

listaLibros = ["Romanticos", "Aventura", "Ciencia Ficcion", "Fantasia"]

listaLibros.append("Drama")
listaLibros[0]

#Actualizar
listaLibros[0] = "Terror"

#Eliminar
listaLibros.remove("Fantasia")
listaLibros.pop(0)
while True:
#Mostrar menu de opciones
    print("\n****** Sisrema de operaciones CRUD ******\n")
    print("1. Mostrar todos los libro")
    print("2. Agregar un libro")
    print("3. Actualizar un libro")
    print("4. Eliminar un libro")
    print("5. Salir \n")

    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("Lista de libros: " , listaLibros)
        elif opcion == 2:
            libro = input("Ingrese el nombre del libro: ")
            listaLibros.append(libro)
            print("El libro: " , libro , " ha sido agregado")
        elif opcion == 3:
            libro = input("Ingrese el nombre del libro a actualizar: ")
            if libro in listaLibros:
                nuevoLibro = input("Ingrese el nuevo nombre del libro: ")
                for i, ele in enumerate(listaLibros):
                    if ele == libro:
                    #listaLibros[listaLibros.index(lib)] = nuevoLibro
                        listaLibros[i] = nuevoLibro
                print("El libro: " , libro , " ha sido actualizado a: " , nuevoLibro)
            else:
                print("El libro: " , libro , " no se encuentra en la lista")
        elif opcion == 4:
            libro = input("Ingrese el nombre del libro a eliminar: ")
            if libro in listaLibros:
                listaLibros.remove(libro)
                print("El libro: " , libro , " ha sido eliminado exitosamente \n")
                print("Lista de libros actualizada: " , listaLibros)
        elif opcion == 5:
            print("Gracias por utilizar el sistema")
        else:
            print("Opción no válida, intente nuevamente")     
    except ValueError:
        print("Error, ingrese un número entero")

