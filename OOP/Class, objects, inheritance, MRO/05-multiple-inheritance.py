class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando")
            

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return(f'Mi habilidad es: {self.habilidad}')  

# Doble herencia
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        #super metodo padre, self metodo hijo
        print(f'Hola, soy: {self.nombre},{self.mostrar_habilidad()} y trabajo en {self.empresa}' )
    


roberto = EmpleadoArtista("Roberto", 43, "ecuatoriana", "pintar", 200, "DYB")
roberto.presentarse()

robertoArtista = Artista("bailar")

inheritance = issubclass(EmpleadoArtista, Artista)
print(inheritance)
inheritance2 = issubclass(Artista, Persona)
print(inheritance2)
instance = isinstance(roberto, EmpleadoArtista)
print(instance)
instance2 = isinstance(roberto, Artista)
print(instance2)
instance3 = isinstance(robertoArtista, Artista)
print(instance3)