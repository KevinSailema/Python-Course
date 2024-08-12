# and, or, not

gas = False
encendido = True
edad = 18

if not gas or encendido or edad > 17:
    print("Puedes avanzar")


# Operaciones de cortocircuito: Son operaciones que se ejecutan de izquierda a derecha
# estas operaciones sirven para ahorrar recursos en la ejecucion, debido a que si se
# ejecuta la primera instancia y retorna FALSO lo demas ya no se ejecuta.
# Operacion or