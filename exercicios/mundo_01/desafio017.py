# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO.
from math import radians, sin, cos, tan

angulo = int(input('informe o angulo: '))
calc = radians(angulo)
seno = sin(calc)
cosseno = cos(calc)
tangente = tan(calc)

print(f'seno, cosseno e tangente do angulo {angulo} respectivamente e {seno:.2f}, {cosseno:.2f}, {tangente:.2f}')