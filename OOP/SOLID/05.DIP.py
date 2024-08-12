# En este ejemplo algo grande depende de
# algo pequeño, esta mal, se corrige con el principio DIP
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Lógica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         # Usamos el diccionario
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para ver si esta en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras desd el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

        def corregir_texto(self, texto):
            # Usamos el verificador para corregir el texto
            pass
