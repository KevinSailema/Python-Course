animal = "    HaPPy pig    "
print(animal.upper())  # Todo el texto a mayúscula
print(animal.lower())  # Todo el texto a minúsula
print(animal.strip().capitalize())  # Capitalize, primera mayuscula
print(animal.title())  # Primer caracter de cada palabra en mayuscula
print(animal.strip())  # Quitar espacios en blanco
print(animal.lstrip())  # Quitar espacios en blanco de la izquierda
print(animal.rstrip())  # Quitar espacios en blanco de la derecha
print(animal.find("PP"))  # Encontrar posicion de cadena de caracteres (Indice)
print(animal.replace("PP", "x"))  # Cambiar cadena de caracteres
print("PP" in animal)  # Buscar cadena de caracteres con Booleano de salida
print("PP" not in animal)  # Buscar cadena de caracteres no se encuentra
