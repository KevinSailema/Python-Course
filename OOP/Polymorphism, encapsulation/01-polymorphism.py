class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(perro.sonido())
hacer_sonido(gato)

print(gato.sonido())

# Duck typing, tipado dinamico

# Cohesion, se adapta enpolimorfismo

num1 = 3
num2 = 4.5

resultado = num1 + num2

print(resultado)
print(type(resultado))

# Duck Typing
# Enlaces dinamicos
# Enlaces estaticos
# Tipo real
# Tipo declarado