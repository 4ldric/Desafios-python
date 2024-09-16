#  FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.

nome = input('digite o seu nome: ')
nome_dividido = nome.split()

print(f'primeiro nome = {nome_dividido[0]} \nultimo nome = {nome_dividido[-1]}')

#RESOLUÇÂO PROFESSOR

n = str(input('digite seu nome completo: ')).strip()
name = n.split()

print(f'seu primeiro nome e {name[0]}')
print(f'seu ultimo nome e {name[len(name)-1]}') 