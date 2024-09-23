# ESCREVA UM PROGRAMA QUE LEIA O NUMERO INTIERO E PEÇA PARA O USUARIO ESCOLHER QUAL SERA A BASE DE CONVERSAO:
# 1 PARA BINARIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL

numero = int(input('escreva um numero inteiro: '))
escolha = int(input('Escolha a conversao informando a numeração: \n1: Binario\n2: Octal\n3: Hexadecimal\ninforme a conversao: '))

if escolha > 3:
    print('informe uma conversao valida!')
elif escolha == 1:
    print(f'{numero} convertido para binario e igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para octal e igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para hexadecimal e igual a {hex(numero)[2:]}')
