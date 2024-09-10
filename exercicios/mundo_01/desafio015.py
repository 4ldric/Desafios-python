# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER E MOSTRE NA TELA SUA PORÇAO INTEIRA

import math

numero_real = float(input("digite um numero: "))
numero_inteiro = math.floor(numero_real)

print(f'O numero {numero_real} tem a parte inteira {numero_inteiro}')