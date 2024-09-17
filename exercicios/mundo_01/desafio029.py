# CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELE E PAR OU IMPAR

numero = int(input('digite um numero: '))

if numero % 2 == 0:
    print(f'o numero {numero} e par')
else:
    print(f'o numero {numero} e impar')