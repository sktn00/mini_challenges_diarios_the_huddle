# Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase derivada Círculo que extienda Figura y
# sobreescriba el método imprimir.
import math


class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print(f"Esta es una figura genérica llamada {self.nombre}")


class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def imprimir(self):
        print(f"Este es un círculo llamado {self.nombre}")
        print(f"Radio: {self.radio}")
        print(f"Área: {self.calcular_area():.2f}")

    def calcular_area(self):
        return math.pi * self.radio**2


# Probamos las clases
figura = Figura("Mi Figura")
figura.imprimir()

print("\n" + "=" * 30 + "\n")

circulo = Circulo("Mi Círculo", 5)
circulo.imprimir()
