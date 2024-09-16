# CRIE UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
#QUANTAS VEZES APARECE A LETRA A
# EM QUE POSIÇÃO ELA APRECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ


#RESOLUÇÂO PROFESSOR
frase = input('digite uma frase: ').upper().strip()

print(f'A letra A aparece {frase.count('A')} vezes')
print(f'A primeira aparição na posição {frase.find('A')+1}')
print(f'A ultima aparição na posição {frase.rfind('A')+1}')

