class Animal:
    def hablar(self):
        print("Sonido genérico")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
