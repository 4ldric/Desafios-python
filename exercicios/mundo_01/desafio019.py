# o professor quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = []

while len(alunos) < 4:
    alunos.append(input('informe o nome dos alunos: '))

random.shuffle(alunos)

print(f'a ordem de apresentação ira ser:\n {alunos}')
