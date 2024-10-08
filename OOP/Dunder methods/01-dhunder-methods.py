# Empieza y termina con 2 guiones bajos, para hacer funciones espciales

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro): # Definir una suma
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

dalto = Persona("Lucas", 21)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 5)

nueva_persona = dalto + pedro + maria

print(nueva_persona.edad)