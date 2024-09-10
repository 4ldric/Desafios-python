# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE D DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.

preco_diaria = 60
preco_km = 0.15
dias_rodados = int(input('informe os dias que ficou com o carro: '))
km_rodados = float(input('informe os Kms rodados: '))

total = preco_diaria * dias_rodados + preco_km * km_rodados

print(f'o total a pagar e de R${total:.2f}')