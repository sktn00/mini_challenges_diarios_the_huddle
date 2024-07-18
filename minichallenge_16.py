# Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro.
# Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.
import math


class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Prueba
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
print(f"Área del círculo: {circulo.calcular_area():.2f}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")
