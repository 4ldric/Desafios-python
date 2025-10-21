# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL MOSTRE QUAL FOI O MAIOR E O PESO LIDO.

contador = 1
lista_pesos = []

while contador <= 5:
    peso = float(input("Informe seu peso: "))
    lista_pesos.append(peso)
    contador += 1
lista_pesos.sort(reverse=True)
print(f'O maior peso da lista foi: {lista_pesos[0]} Kg\n e o menor peso lido: {lista_pesos[-1]} Kg')

