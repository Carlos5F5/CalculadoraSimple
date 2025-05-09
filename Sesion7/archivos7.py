try:
    archivo = open(r"data_estudiante.xlsx", "r")
    print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe")
finally:
    if 'archivo' in locals():
        archivo.close()


