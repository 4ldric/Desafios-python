# FAÇA UM PROGRAMA QUE MOSTRE NA TELA MA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATE 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.
from time import sleep

contagem = 10

print('Preparem-se para a contagem regressiva')

for i in range(contagem, -1, -1):
    print(i)
    sleep(1)
print('Fogos estourados, kabum pei pow kabum')