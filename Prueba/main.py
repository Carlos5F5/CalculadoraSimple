from persona import Persona
from cuenta_bancaria import CuentaBancaria
from empleado import Empleado
from animal import Perro, Gato

if __name__ == "__main__":
    # Persona
    p = Persona("Carlos", 28)
    p.saludar()

    # Cuenta bancaria
    cuenta = CuentaBancaria("Carlos", 1000)
    cuenta.depositar(500)
    cuenta.mostrar_saldo()

    # Empleado
    e = Empleado("Lucía", 32, "Ingeniera de software")
    e.presentarse()

    # Animales
    animales = [Perro(), Gato()]
    for animal in animales:
        animal.hablar()
