#  Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial

numero = int(input("Digite o numero para saber seu fatorial: "))
f = 1
contador = numero

print(f'calculando {numero}! = ', end='')

while contador > 0:
    print(f'{contador}')
    print(' x ' if contador > 1 else ' = ', end="")
    f *= contador
    contador -= 1

print(f'{f}')