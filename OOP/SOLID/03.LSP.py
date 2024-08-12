# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"

# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

# En este principio se define todo lo de una clase (codigo legible)
class Ave:
    pass

class AveVoladora(Ave):
    def volar(delf):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass