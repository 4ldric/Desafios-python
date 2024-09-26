# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE E OU NAO UM NUMERO PRIMO

numero = int(input('digite um numero: '))

if numero % 1 == 0 and numero % 2 == 0:
    print(f'O numero {numero} não e um numero primo')

else:
    print(f'O numero {numero} e um numero primo')