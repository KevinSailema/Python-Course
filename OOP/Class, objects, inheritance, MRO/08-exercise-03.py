class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()
    