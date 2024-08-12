from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar (self):
        pass   
    
class Comedor(ABC):
    @abstractmethod
    def comer (self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir (self):
        pass

class Humano(Trabajador, Durmiente, Comedor):

    def comer (self):
        print("Humano comiendo")

    def trabajar (self):
        print("Humano trabajando")

    def dormir (self):
        print("Humano durmiendo")

class Robot(Trabajador):

    def trabajar (self):
        print("Robot trabajando")

robot = Robot()
robot.trabajar()