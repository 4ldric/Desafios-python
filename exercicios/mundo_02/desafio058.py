# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numero_secreto = randint(0,10)
tentativas = 1

print("== bem vindo ao numero secreto == ")
print('estou pensando em um numero entre 0 e 10, tente adivinha qual o numero')

palpite = int(input("Qual e seu palpite? "))

while palpite != numero_secreto:
    if palpite > numero_secreto:
        palpite = int(input("seu palpite e maior que o numero secreto, tente novamente: "))
        tentativas += 1
    else:
        palpite = int(input("seu palpite e menor que o numero secreto, tente novamente: "))
        tentativas += 1

if tentativas < 2:
    mensagem = 'tentativa'
else:
    mensagem = 'tentativas'

print(f"Parabens, voce descobriu o numero {numero_secreto} com {tentativas} {mensagem}.")
