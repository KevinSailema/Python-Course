class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando...')

print("Datos del estudiante:")
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
grado = input("Escribe tu grado: ")

estudiante1 = Estudiante(nombre, edad, grado)
print(f"""
      Datos del estudiante: \n
      Nombre: {estudiante1.nombre} \n
      Edad: {estudiante1.edad} \n
      Grado: {estudiante1.grado} \n
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()