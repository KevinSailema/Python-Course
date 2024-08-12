# Decorators, funcion que agrega codigo extra.

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Después de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Dalto")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

# Bien escrito, reemplazo a lo comentado (ln10-ln14)
@decorador
def saludo():
    print("Hola Dalto como andas")

saludo()
