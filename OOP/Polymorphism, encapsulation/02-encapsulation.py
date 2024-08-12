class MiClase:
    def __init__(self):
      self.__atributo_privado = "Valor"

    def __hablar(self):
       print("Hola, como estas")

objeto = MiClase()
print(objeto.__hablar())

