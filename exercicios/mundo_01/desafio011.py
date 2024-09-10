# FAÇA UM ALGORITMO QUE LEIA O PREÇO D EUM PORDUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

preco = float(input('informe o preço: '))
desconto = preco - (preco * 0.05)


print(f'valor com desconto {desconto:.2f}')