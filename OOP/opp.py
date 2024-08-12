print("Hello World")
# Programar imperativamente
perro = "Woof"

# argumentos de funciones, x en habla
# resultado de una funcion, range x
# Functional pgrm. decorators.

def habla (x):
    for i in range (x):
        print(perro)

habla (3)

class Animal:
    def __init__(self) -> None:
        self.sonido = None
        
    def habla(self,x : int) -> None: #None, establecer lo que retorna
        for i in range (x):
            print(self.sonido)

class Perro(Animal):
    def __init__(self, raza : str) -> None:  #Argumento: Usuario pasa str.
        self.sonido = "Woof"
        self.raza = raza
        self.peso = None

    def setPeso(self, peso : float) -> None:
        self.peso = peso

    def getPeso(self) -> float:
        return self.peso
    
class Gato(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.sonido = "Miau"

# Definir metodos
# Self.name definir atributos    

animales = [Perro("Huskie"), Perro("Poodle"), Perro("Akita"), Gato()]

for animal in animales:
    animal.habla(1)

