class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: ${self.__saldo}")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
