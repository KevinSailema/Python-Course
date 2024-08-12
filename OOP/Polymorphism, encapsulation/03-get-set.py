class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

dalto = Persona("Lucas", 21)
# Para obtener un nombre protegido o privado (__)
nombre = dalto.get_nombre()
print(nombre)
# Para establecer un nuevo nombre a algo protegido o privado
dalto.set_nombre("Pepe")
# Se obtiene ese nuevo nombre
nombre = dalto.get_nombre()
print(nombre)