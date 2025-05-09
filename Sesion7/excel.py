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


datos = leer_Excel(ruta)
print(datos)









""" df = pd.DataFrame(mydataset)
print(type(df))
print(df)
 """

