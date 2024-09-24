# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPO COM VOCE
from random import randint
from time import sleep

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print(f'{' JOKENPO ':=^30}')

jogador = int(input('''Escolha sua jogada
[0]: PEDRA
[1]: PAPEL
[2]: TESOURA 
alternativa: '''))

if jogador > 2:
    print('INFORME APENAS OPÇÂO VALIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-='*20)
    print(f'Computador jogou { lista[computador]} \nJogador jogou {lista[jogador]}')
    print('-='*20)

    if computador == 0 and jogador == 2:
        print('COMPUTADOR VENCE\n')
    elif computador == 1 and jogador == 0:
        print('COMPUTADOR VENCE\n')
    elif computador == 2 and jogador == 1:
        print('COMPUTADOR VENCE\n')
    elif computador == jogador:
        print('EMPATE\n')
    else:
        print(f'JOGADOR VENCE\n')


#   RESOLUÇÂO PROFESSOR

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

computer = randint(0,2)
print('''Escolha sua jogada
[0]: PEDRA
[1]: PAPEL
[2]: TESOURA''')
player = int(input('qual sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {lista[computer]} \nJogador jogou {lista[player]}')
print('-=' * 11)

if computer == 0:  # COmputador jogou pedra
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
elif computer == 1:
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
elif computer == 2:
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('EMPATE')