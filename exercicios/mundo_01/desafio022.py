# FAÇA UM PROGRAMA QUE LEIA UM NUMERO de 0 a 9999 e mostre na tela cada u dos digitos separados.

numero = int(input('digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMIlhar: {milhar}')


