# ESCREVA UM PROGRAMA QUE LEIA  AVELOCIDADE D EUM CARRO, SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE FOI MULTADO. A MULTAVAI CUSTAR R$7 POR CADA KM ALIME DO LIMITE.

from random import randint

km = randint(0,150)

if km > 80:
    print(f'atenção: {km}Km/h')
    multa = (km - 80) * 7
    print(f'Voce foi multado, sua divida e de R${multa:.2f}')
else:
    print('livre')