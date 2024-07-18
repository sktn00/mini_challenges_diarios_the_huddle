# Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Usamos __ para hacer el saldo "privado"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositaron {cantidad} euros. Nuevo saldo: {self.__saldo} euros")
        else:
            print("La cantidad a depositar debe ser positiva")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.__saldo >= cantidad:
                self.__saldo -= cantidad
                print(
                    f"Se retiraron {cantidad} euros. Nuevo saldo: {self.__saldo} euros"
                )
            else:
                print("Saldo insuficiente")
        else:
            print("La cantidad a retirar debe ser positiva")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.__saldo} euros")


# Probamos la clase
cuenta = CuentaBancaria("Juan Pérez", 1000)

cuenta.consultar_saldo()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)  # Esto debería fallar
cuenta.depositar(-100)  # Esto debería fallar
cuenta.consultar_saldo()
