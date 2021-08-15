from carro import Carro
from pista import Pista
from os import system
import time


def inicio():
    print('')
    print('           BIENVENIDO')
    print('')
    print('        Elige una pista')
    print('')
    print('       1. Pista Silverstone')
    print('       2. Pista Interlagos')
    print('       3. Pista Monza')
    print('       4. Pista Suzuka')
    print(' ')
    opcion = input()
    while opcion not in ('1', '2', '3', '4'):
        opcion = input('  -->')
    return opcion


system('cls')
opcion = inicio()

if opcion == '1':
    pista = Pista('Silverstone', 8, 4000, '.')
elif opcion == '2':
    pista = Pista('Interlagos', 5, 4500, '-')
elif opcion == '3':
    pista = Pista('Monza', 6, 5000, '_')
elif opcion == '4':
    pista = Pista('Suzuka', 7, 5500, '~')

jugadores = ['Lewis', 'Valterri', 'Max', 'Sergio',
             'Lando', 'Daniel', 'Lance', 'Sebastian']
conductores = []

for i in range(pista.carriles):
    carro = Carro(jugadores[i])
    conductores.append(carro)

for i in range(pista.carriles):
    pista.poner_carro(conductores[i], i, conductores[i].metro, pista.metros)

system('cls')

pista.mostrar()

input('Elige un conductor y pulsa Enter ')
meta = []
while True:
    system('cls')

    for conductor in conductores:
        if conductor.metro > pista.metros - 100:
            meta.append(conductor)

    for i in range(pista.carriles):
        pista.poner_carro(pista.ornamento, i,
                          conductores[i].metro, pista.metros)

    for i in range(pista.carriles):
        conductores[i].avanzar()
        pista.poner_carro(conductores[i], i,
                          conductores[i].metro, pista.metros)

    if len(meta) > (int(pista.carriles)-1):
        break

    pista.mostrar()
    time.sleep(1)

pista.mostrar()

podio = []


for i in meta:
    if i not in podio:
        podio.append(i)
print('Ganadores', end=' ')
archivo = open('historial.txt', 'a')
archivo.write(f'\n Podio de la pista {pista.nombre} \n')
for i in range(0, 3):
    print(f'{i+1}. {podio[i]}', end=' ')
    archivo.write(f'{i+1}. {podio[i]} ')
archivo.write('\n')
archivo.close()

print()
