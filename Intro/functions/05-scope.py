saludo = "Hola global"

def saludar():
    global saludo  # Citar variables globales
    saludo = "Hola Mundo"
    print(saludo)
    
def saludarChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

print(saludo)
saludar()
print(saludo)

# Variables globales, mala practica.
