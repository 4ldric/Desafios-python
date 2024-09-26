#  DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA DAQUELES APENAS QUE FOREM PARES. SE O VALOR FOR IMPAR DESCONSIDERE
soma = 0

for numero in range(0,6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n

print(f'a soma dos numeros pares e igual a: {soma}')