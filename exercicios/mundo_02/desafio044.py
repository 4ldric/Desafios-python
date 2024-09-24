# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# A VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# A VISTA NO CARTAO: 5% DE DESCONTO
# EM ATE 2X NO CARTAO: PREÇO NORMAL
# 3X OU MAIS NO CARTAO: 20% JUROS

valor_original = float(input('informe o preço do produto: '))
pagamento = int(input('Informe o tipo do pagamento\n[1]: dinheiro / cheque \n[2]: Cartão \nopção: '))
desconto = 0

if pagamento != 1 and pagamento != 2:
    print('informe uma opção de pagamento valida!!')
elif pagamento == 1:
    desconto = valor_original - valor_original * 0.10
    print(f'O valor total a pagar e: R${desconto:.2f}')
elif pagamento == 2:
    opcao = int(input('informe a forma de pagamento no cartao: \n[1]: a vista \n[2]: parcelado \nOpção: '))
    if opcao == 1:
        desconto = valor_original - valor_original * 0.05
        print(f'O valor total a pagar e: R${desconto:.2f}')
    elif opcao == 2:
        parcelas =  int(input('Informe o total de parcelas: '))
        if parcelas <= 2:
            print(f'O valor de cada parcela em 2x sera de: R${valor_original / 2:.2f}')
        else:
            juros = valor_original * 1.20
            print(f'O valor de cada parcela em {parcelas}X sera de: R${juros / parcelas:.2f} totalizando R${juros:.2f}')
