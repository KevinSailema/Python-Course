"""Calc on python"""

n1 = input("Ingresa el primer número ")  # input recibe dato del usuario
n2 = input("Ingresa el segundo número ")  # input recibe dato del usuario

n1 = int(n1)
n2 = int(n2)

add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

message = f"""
Para los números {n1} y {n2}
El resultado de la suma es {add}
El resultado de la resta es {sub}
El resultado de la multiplicación es {mult}
El resultado de la división es {div}
"""
print(message)
