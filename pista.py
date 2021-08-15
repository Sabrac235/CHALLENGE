
class Pista:

    def __init__(self, nombre, carriles, metros, ornamento):
        self.nombre = nombre
        self.carriles = carriles
        self.metros = metros
        self.ornamento = ornamento
        self.pista = []
        for i in range(carriles):
            self.pista.append([ornamento] * (metros//100))

    def poner_carro(self, carro, carril, metro, metros):
        if metro >= metros:
            pass
        else:
            self.pista[carril][(metro//100)] = carro

    def mostrar(self):
        print('  Pista de {}'.format(self.nombre).center(self.metros))
        print('  || SALIDA' + ('=' * ((self.metros//50)) + '||META'))
        for x in range(self.carriles):
            print(' ', end=' ')
            for j in range((self.metros//100)):
                print(self.pista[x][j], end=' ')
            print()
