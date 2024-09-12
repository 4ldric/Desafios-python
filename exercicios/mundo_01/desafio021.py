 # CRIE UM PROGRMA QUE LEIE O NOME COMPLETO DE UMA PESSOA E MOSTRE:
 # O NOME COM TODAS AS LETRAS MAISCULAS
 # O NOME COM TODAS MINUSCULAS
 # QUANTAS LETRAS AO TODO SEM CONSIDERAR ESPAÇOS
 # QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('nome completo: ')
nome_dividido =  nome.split()

print(f'nome: {nome.upper()}')
print(f'nome: {nome.lower()}')

print(f'total de letras {len(nome.replace(" ", ""))}') # substituindo os espaços para nada.

print(f'letras no primeiro nome: {len(nome_dividido[0])}')

