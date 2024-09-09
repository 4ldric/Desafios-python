# FAÇA UM ALGORITMO QUE LEIA O PREÇO D EUM PORDUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

preco = float(input('informe o preço: '))
desconto = preco * 0.05
novo_preco = preco - desconto

print(f'valor com desconto {novo_preco:.2f}')