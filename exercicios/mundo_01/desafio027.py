# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR ESCOLHER UM NUMERO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR

from random import randint
from time import sleep #importando modulo de pausa de execução por um periodo determinado

numero_aleatorio = randint(0,5)

print('-=-' * 20) # enfeitando o game
print('Bem vindo, tente adivinhar o numero entre 0 e 5')
print('-=-' * 20)

numero = int(input('informe o numero: '))

print('Aguarde...')
sleep(2) # pausa de 2 segundos

if numero > 5:
    print('digite apenas numeros de 0 a 5')
elif numero == numero_aleatorio:
    print(f'parabens voce acertou, o numero secreto e {numero_aleatorio}')
else:
    print(f'Voce errou, o numero secreto era {numero_aleatorio}')

print('Fim')