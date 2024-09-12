# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM O NOME 'SANTO'  

cidade = input('digite o nome da cidade: ')
cidade_dividida = cidade.split()

print(f'A cidade se inicia com santo?: {'santo' in cidade_dividida[0]}')