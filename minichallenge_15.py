# Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor con un método para describir el motor.
class Motor:
    def __init__(self, tipo, cilindrada):
        self.tipo = tipo
        self.cilindrada = cilindrada

    def describir(self):
        return f"Motor {self.tipo} de {self.cilindrada} cc"


class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_motor(self):
        print(f"El {self.marca} {self.modelo} tiene un {self.motor.describir()}")


# Prueba
motor_sedan = Motor("gasolina", 2000)
mi_auto = Auto("Toyota", "Corolla", motor_sedan)
mi_auto.describir_motor()
