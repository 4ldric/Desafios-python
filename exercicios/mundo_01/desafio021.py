 # CRIE UM PROGRMA QUE LEIE O NOME COMPLETO DE UMA PESSOA E MOSTRE:
 # O NOME COM TODAS AS LETRAS MAISCULAS
 # O NOME COM TODAS MINUSCULAS
 # QUANTAS LETRAS AO TODO SEM CONSIDERAR ESPAÇOS
 # QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('nome completo: ')
nome_dividido =  nome.split()

print(f'nome: {nome.upper()}')
print(f'nome: {nome.lower()}')

print(f'total de letras {len(nome.replace(" ", ""))}').split() # substituindo os espaços para nada.

print(f'letras no primeiro nome: {len(nome_dividido[0])}')

# Resolução professor

name = str(input('Digite seu nome completo: '))  # remove os espaços laterais
print(f'seu nome tem ao todo {len(name) - name.count(" ")}')
print(f' seu primeiro nome tem {name.find(' ')}')