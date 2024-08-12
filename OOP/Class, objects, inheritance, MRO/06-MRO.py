class A:
    def hablar(self):
        print("Hola desde A")

class B:
    def hablar(self):
        print("Hola desde B")

class F:
    def hablar(self):
        print("Hola desde F")

class C:
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()
# Imprimir esquema de MRO
print(D.mro())
d.hablar()

F.hablar(d)  # Creacion de objeto con propiedades "d"

