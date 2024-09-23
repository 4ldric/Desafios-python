# ESCREVA UM PROGRAMA PARA APROVAR UM EMPRESTIMO BANCARIO PARA A OMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
# CALUCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NAO PODE EXCEDER 30% DO SALARIO OU ENTAO O EMPRESTIMO SER NEGADO

print('-=-' * 10)
print('conquiste sua casa propria')
print('-=-' * 10)

valor_casa = float(input('informe o valor da casa: '))
salario = float(input('informe seu salario: '))
anos_pagamento = int(input('quantos anos para concluir o pagamento? '))
prestacao = valor_casa / (anos_pagamento * 12)
renda_minima = salario * 0.30

print(f'A mensalidade do financiamento de uma casa de R${valor_casa:.2f} em {anos_pagamento} anos e  R${prestacao:.2f}')

if prestacao > renda_minima:
    print('Infelizmente o emprestimo foi Negado!')
else:
    print('Parabens, emprestimo aprovado!')
