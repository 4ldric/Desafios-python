# Calculadora

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

while True:
    escolha = input ('''
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
\nescolha uma opção: ''')
    
    if escolha == '1':
        soma = n1 + n2
        print(f'A soma entre os numeros {n1} + {n2} é: {soma}')
    elif escolha == '2':
        multi = n1 * n2
        print(f'A multiplicação entre os numeros {n1} x {n2} é: {multi}')
    elif escolha == '3':
        maior_numero = 0
        if n1 > n2:
            maior_numero = n1
        else:
            maior_numero = n2
        print(f'O maior numero entre {n1} e {n2} é: {maior_numero}')
    elif escolha == '4':
        n1 = float(input('digite o novo valor primario: '))
        n2 = float(input('digite o novo valor secundario: '))
    elif escolha == '5':
        print('saindo...')
        break
    else:
        print("Opção invalida, tente novamente..")