# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO

salario = float(input('digite seu salario: '))
aumento = salario * 0.15
novo_salario = salario + aumento

print(f'seu novo salario e {novo_salario:.3f}')