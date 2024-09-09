# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA A SUA TABUADA

valor = int(input('digite um numero: '))

for numero in range(1, 11, 1): 
    print(f"{valor} x {numero} = {valor * numero}")
