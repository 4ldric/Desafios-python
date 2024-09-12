# FAÇA UM PROGRAMA QUE LEIA UM NUMERO de 0 a 9999 e mostre na tela cada u dos digitos separados.

numero = input('digite um numero: ')

if len(numero) < 4:
    print(f'Unidade: {numero[2]} \nDezena: {numero[1]} \nCentena: {numero[0]}')
   
else:
    print(f'Unidade: {numero[3]} \nDezena: {numero[2]} \nCentena: {numero[1]} \nMIlhar: {numero[0]}')


