# Function print
print("")
# def para definir una funcion, seguido del nombre, ()
# hay que llamar otra funcion para ejecutar
def hola(nombre, apellido="Feliz"):  # Dentro del (), variables obligatorias
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")

# Llamada a la funcion
hola("Nicolas" , "Schurmann")
hola("Chanchito", "Feliz")
hola("Chanchito")

# dentro de la funcion parametros, fuera argumentos.

# Agregar orden a los parametros
hola(apellido="Schurmann", nombre="Nicolas")
