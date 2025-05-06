class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def mostrar_saldo(self):
        print(f"💰 Saldo de {self.titular}: {self.saldo}")
