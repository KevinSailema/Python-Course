class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    @property  #podemos ocultar el metodo get para obtener
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter     
    def nombre(self):
        del self.__nombre

dalto = Persona("Lucas", 21)
# Para obtener un nombre protegido o privado (__)
nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"
nombre = dalto.nombre
print(nombre)

del dalto.nombre

print("Finalizacion")