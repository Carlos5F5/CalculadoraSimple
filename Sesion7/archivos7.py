try:
    archivo = open(r"C:\DocumentosDeRAIZ\Ingenierìa\LenguajesProgramación\Python\PythonDeveloper\Sesion7\archivos7.txt", "r")
    print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe")
finally:
    if 'archivo' in locals():
        archivo.close()

