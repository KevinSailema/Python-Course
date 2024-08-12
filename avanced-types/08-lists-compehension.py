usuarios = [["Chanchito", 4], 
            ["Felipe", 1], 
            ["Pulga", 5]
]

# Pasar lista de usuarios a lista de nombres
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

# Forma mas facil
# name = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]

# Filtrar listas
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# Filtrar listas y transformada
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)