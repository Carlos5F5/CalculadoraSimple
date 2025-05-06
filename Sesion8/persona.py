# archivo: persona.py
class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    def saludar(self):  # Método
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

