import random


class Carro:

    def __init__(self, nombre):
        self.nombre = nombre
        self.metro = 0

    def __str__(self):
        return self.nombre

    def avanzar(self):
        self.metro += (random.randint(1, 6)*100)
