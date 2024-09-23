# ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIRO E COMPARE-OS, MOSTRANDO NA TLA UMA MENSAGEM:
# O PRIMEIRO VALOR E MAIOR, O SEGUNDO VALOR E MAIOR OU NAO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS

n1 = int(input('informe o primeiro numero '))
n2 = int(input('informe o segundo numero '))

if n1 > n2:
    print('o primeiro valor e MAIOR')
elif n2 > n1:
    print('o segundo valor e MAIOR')
else:
    print('os valores sao iguais')
