# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA E UM PALINDROMO, DESCONSIDERANDO OS ESPAÇOS

frase = input('digite uma frase: ')

texto = frase.lower().replace(' ', '').replace('.', '').replace(',', '')
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print('esta frase e um palindromo')
else:
    print('esta frase nao e um palindromo')