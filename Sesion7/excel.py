ruta = "data_estudiante.xlsx"
import pandas as pd

""" mydataset = {
    'Nombre': ['Carlos', 'Johana', 'Rocio'],
    'Apellido': ['Franco', 'Poveda', 'Satian'],
    'Edad': [20, 18, 44]
} """


def leer_Excel(file):

    try:
        df = pd.read_excel(file)
        return df
    
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Error: {e}")

def escribir_Excel(file):
    try:
        #Leer el archivo de Excel
        df = pd.read_excel(file)

        #Capturar  nuevos datos
        datosEstu = []
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        profesion = input("Ingrese la profesion: ")

        datosEstu.append(nombre)
        datosEstu.append(edad)
        datosEstu.append(profesion)

        nuevaFila = pd.DataFrame
    except Exception as e:
        print(f"Error: {e}")


datos = leer_Excel(ruta)
print(datos)









""" df = pd.DataFrame(mydataset)
print(type(df))
print(df)
 """

