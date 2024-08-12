mascotas = ["Wolfang",
            "Pelusa", 
            "Pulga", 
            "Felipe",
            "Pulga" 
            "Chanchito feliz"
            ]

# Agregar elementos
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # Agregar al final
print(mascotas)

mascotas.remove("Pulga") # Solo elimina el primero
mascotas.pop(1) # Eliminar el ultimo elemento del arreglo con (vacio)
del mascotas[0] # otro metodo para eliminar
mascotas.clear() # Eliminar todo
print(mascotas)