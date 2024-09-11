# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO.
import math

angulo = int(input('informe o angulo: '))
calc = math.radians(angulo)
seno = math.sin(calc)
cosseno = math.cos(calc)
tangente = math.tan(calc)

print(f'seno, cosseno e tangente do angulo {angulo} respectivamente e {seno}, {cosseno}, {tangente}')