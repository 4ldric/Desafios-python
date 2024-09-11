# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO
import random

lista = []

while len(lista) < 4:
    lista.append(input("digite o nome do aluno: "))

escolhido = random.choice(lista)

print(f'O aluno escolhido para limpar o quadro foi: {escolhido}')
