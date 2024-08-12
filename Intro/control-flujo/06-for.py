# For: Sirve para iterar, buscar elementos.

for numero in range(5):
    print(numero, numero * 'hola mundo')

# Otro ejemplo
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no se encontro el numero buscado")

# Iterables: Numeros, Listas, Tuplas, Strings.

# Iterando caracteres
for char in "Ultimate python":
    print(char)