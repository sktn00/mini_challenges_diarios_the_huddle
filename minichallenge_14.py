# Polimorfismo: Crea una clase base Animal con un método hacerSonido y una clase derivada Perro que sobrescriba este método.
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido genérico")


class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: Guau!")


# Prueba
animal = Animal()
perro = Perro()

animal.hacer_sonido()
perro.hacer_sonido()
