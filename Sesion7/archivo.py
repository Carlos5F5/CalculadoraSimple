#Trabajo con archivos y errores

rutaarchivo = "archivos7.txt"

def leerachivo(file):
    try: 
        archivo = open(file, "r" )
        contenido = archivo.read()
        archivo.close()
        return contenido

    except FileNotFoundError:
        print("El archivo no existe")



def escribirarchivo(filew):
    try: 
        nuevoargumento = input( "Escribe el nuevo argumento: ")
        archivo = open(filew, "a" )
        contenido = archivo.write("\n" + nuevoargumento)
        archivo.close()
        return contenido

    except FileNotFoundError:
        print("El archivo no existe")

response = leerachivo(rutaarchivo)
print(response)


filewescribirarch = escribirarchivo(rutaarchivo)
