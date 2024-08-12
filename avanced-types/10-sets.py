# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
primer.add(5)
primer.remove(1)
print(primer)

segundo = [3,4,5]
segundo = set(segundo)
print(primer | segundo)  # Operador Union
print(primer & segundo)  # Operador interseccion
print(primer - segundo)  # Diferencia
print(primer ^ segundo) #Diferencia simetrica (Eliminar duplicados)


if 5 in segundo:
    print("Hola Mundo")
