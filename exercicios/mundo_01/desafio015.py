# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER E MOSTRE NA TELA SUA PORÇAO INTEIRA

from math import floor

numero_real = float(input("digite um numero: "))
numero_inteiro = floor(numero_real)

print(f'O numero {numero_real} tem a parte inteira {numero_inteiro}')

# SEM IMPORTAÇÃO DE MODULOS

numero = float(input("digite um numero: "))

print(f'O numero {numero} tem a parte inteira {int(numero)}')
