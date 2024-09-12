# CRIE UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
#QUANTAS VEZES APARECE A LETRA A
# EM QUE POSIÇÃO ELA APRECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

frase = input('digite uma frase: ')

print(f'Primeira aparição: {frase.find('a')} \nUltima aparição: {frase.count('a',0,13)}')