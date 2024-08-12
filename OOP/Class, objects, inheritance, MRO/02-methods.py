class Celular():
    def __init__(self, marca, modelo, camara):    # Metodo constructor, se ejecuta automaticamente
        self.marca = marca   #self.marca es una propiedad de self
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas haciendo un llamada desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MPS")

print(celular1.marca)
print(celular2.marca)

celular1.llamar()
celular2.cortar()
