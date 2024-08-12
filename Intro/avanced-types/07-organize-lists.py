numeros = [2, 4, 1, 45, 75, 22]

numeros.sort() # Sort, ordenar
numeros.sort(reverse = True) # Sort, ordenar, descendente
numeros2 = sorted(numeros)  # Devuelve una nueva lista
numeros3 = sorted(numeros, reverse = True) # Reversa
print(numeros)
print(numeros2)
print(numeros3)


usuarios = [["Chanchito", 4], 
            ["Felipe", 1], 
            ["Pulga", 5]
]

def ordena(elemento):
    return elemento[1]
    
usuarios.sort(key= ordena, reverse= True)
print(usuarios)

# De mejor forma

usuarios.sort(key=lambda pf: pf[1] , reverse= False)
print(usuarios)