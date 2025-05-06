# Clase completa: Los 4 pilares de la Programación Orientada a Objetos (POO) en Python

# -----------------------------
# 1. Abstracción
# -----------------------------
# Consiste en modelar objetos del mundo real en clases, capturando solo lo esencial
# Creamos una clase base para representar una persona

class Persona:
    def __init__(self, nombre, edad):
        # __init__ es el método constructor
        # Se ejecuta automáticamente al crear un objeto
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creamos un objeto
persona1 = Persona("Carlos", 28)
persona1.presentarse()


# -----------------------------
# 2. Encapsulamiento
# -----------------------------
# Consiste en ocultar los detalles internos del objeto, exponiendo solo lo necesario
# Los atributos privados usan un guion bajo para indicar que no deberían tocarse directamente

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es ${self.__saldo}")

cuenta = CuentaBancaria("Lucia", 500)
cuenta.depositar(150)
cuenta.mostrar_saldo()
# cuenta.__saldo  # Esto dará error si se intenta acceder directamente


# -----------------------------
# 3. Herencia
# -----------------------------
# Permite que una clase herede métodos y atributos de otra
# Clase base: Persona (ya creada), Clase derivada: Estudiante

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de Persona
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

estudiante1 = Estudiante("María", 21, "Ingeniería")
estudiante1.presentarse()
estudiante1.estudiar()


# -----------------------------
# 4. Polimorfismo
# -----------------------------
# Permite que diferentes clases compartan métodos con el mismo nombre pero con comportamiento diferente

class Animal:
    def hablar(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro dice: Guau")

class Gato(Animal):
    def hablar(self):
        print("El gato dice: Miau")

animales = [Perro(), Gato(), Animal()]
for animal in animales:
    animal.hablar()  # Cada uno ejecuta su versión del método "hablar"


# -----------------------------
# Notas adicionales
# -----------------------------
# - self: palabra clave que representa al objeto actual
# - __init__: método constructor para inicializar valores
# - super(): llama métodos de la clase padre
# - Los métodos son funciones dentro de clases que interactúan con los datos del objeto
