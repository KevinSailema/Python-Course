class CelularDemo():
    # Creando atributos estaticos, para todo los objetos son iguales
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

celular1 = CelularDemo() #Instancia de clase, si instancio creo un objecto
print(celular1.modelo) #Preguntar propiedades con "."

celular2 = CelularDemo()
celular3 = CelularDemo()
celular4 = CelularDemo()

celular3.camara = "12MP"
print(celular3.camara)
print(celular3)

# Forma correcta de crear un objeto
class Celular():
    def __init__(self, marca, modelo, camara):    # Metodo constructor, se ejecuta automaticamente
        self.marca = marca   #self.marca es una propiedad de self
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MPS")

print(celular1.marca)
print(celular2.marca)
