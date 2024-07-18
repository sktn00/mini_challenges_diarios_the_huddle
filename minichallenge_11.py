# Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas.
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")


# Test the class
punto1 = Punto2D(3, 4)
punto2 = Punto2D(-1, 2)

punto1.imprimir_coordenadas()
punto2.imprimir_coordenadas()
