# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO

salario = float(input('digite seu salario: R$'))
aumento = salario + (salario * 0.15)


print(f'seu novo salario e R${aumento:.2f}')