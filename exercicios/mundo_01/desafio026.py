#  FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.

nome = input('digite o seu nome: ')
primeiro_nome = nome.split()
ultimo_nome = nome.split()

print(f'primeiro nome = {primeiro_nome[0]} \nultimo nome = {ultimo_nome[-1]}')