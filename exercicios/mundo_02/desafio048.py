# FAÇA um programa que calcule a soma entre todos os numeros impares que sao multipos de tre e que se encontram no intervalo de 1 ate 500

inicio = 1
soma = 0

for numero in range(inicio, 501, 2):
        if numero % 3 == 0:
            soma += numero
print(f'a soma dos numeros impares entre 1 e 500 e: {soma}')